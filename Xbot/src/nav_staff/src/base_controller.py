#!/usr/bin/env python
#coding=utf-8
""" 
底盘移动控制软件

Copyright (c) 2016 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot. 

"""
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Path
#from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
import PyKDL
import numpy
from geometry_msgs.msg import Quaternion
import copy
import CVlib
import Queue
from threading import Lock
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PointStamped
  
  
class ClearParams:
 def __init__(self):
  rospy.loginfo('clear primaray parameters')
  rospy.delete_param('~PlanTopic')
  rospy.delete_param('~OdomTopic')
  rospy.delete_param('~MotionTopice')
  rospy.delete_param('~PathBias')
  rospy.delete_param('~MaxLinearSP')
  rospy.delete_param('~MinLinearSP')
  rospy.delete_param('~MaxAngularSP')
  rospy.delete_param('~MinAngularSP')
  rospy.delete_param('~AngularBias')
  rospy.delete_param('~AngularFree')
  rospy.delete_param('~PositionFree')
  rospy.delete_param('~PublishFrequency')
  rospy.delete_param('~PredictDistance')
  
  
class BaseController:
 def __init__(self):
  self.define()
  rospy.Subscriber('%s'%self.OdomTopic, Pose, self.OdomCB)
  rospy.Subscriber('%s'%self.PlanTopic, Path, self.PlanCB)
  rospy.Timer(rospy.Duration(self.PublishFrequency), self.PublishCB)
  rospy.Timer(rospy.Duration(self.PublishFrequency*100), self.LogCB)
  rospy.Subscriber('/move_base/current_goal', PoseStamped, self.GoalCB)
  #rospy.Subscriber('%s'%self.ScanTopic, Path, self.ScanCB)
  rospy.spin()
  
 def define(self):
  
  #parameters
  if not rospy.has_param('~PlanTopic'):
   rospy.set_param('~PlanTopic','/move_base/NavfnROS/plan')
  self.PlanTopic = rospy.get_param('~PlanTopic')

  if not rospy.has_param('~OdomTopic'):
   rospy.set_param('~OdomTopic','/turtlebot_position_in_map')
  self.OdomTopic = rospy.get_param('~OdomTopic')

  if not rospy.has_param('~MotionTopice'):
   rospy.set_param('~MotionTopice','/cmd_vel_mux/input/navi')   #cmd_vel_mux/input/navi #/navigation_velocity_smoother/raw_cmd_vel
  self.MotionTopice = rospy.get_param('~MotionTopice')

  if not rospy.has_param('~PathBias'): #how accuracy the robot will attemped to move to next path goal
   rospy.set_param('~PathBias', 0.10) 
  self.PathBias = rospy.get_param('~PathBias')

  if not rospy.has_param('~MaxLinearSP'):
   rospy.set_param('~MaxLinearSP', 0.4)
  self.MaxLinearSP = rospy.get_param('~MaxLinearSP')

  if not rospy.has_param('~MinLinearSP'):
   rospy.set_param('~MinLinearSP', 0.01)
  self.MinLinearSP = rospy.get_param('~MinLinearSP')
  
  if not rospy.has_param('~MaxAngularSP'):
   rospy.set_param('~MaxAngularSP', 0.4)
  self.MaxAngularSP = rospy.get_param('~MaxAngularSP')

  if not rospy.has_param('~MinAngularSP'):
   rospy.set_param('~MinAngularSP', 0.05)
  self.MinAngularSP = rospy.get_param('~MinAngularSP')

  if not rospy.has_param('~AngularBias'):
   rospy.set_param('~AngularBias', 0.25)
  self.AngularBias = rospy.get_param('~AngularBias')

  if not rospy.has_param('~AngularFree'):
   rospy.set_param('~AngularFree', 0.1)
  self.AngularFree = rospy.get_param('~AngularFree')

  if not rospy.has_param('~PositionFree'):
   rospy.set_param('~PositionFree', 0.05)
  self.PositionFree = rospy.get_param('~PositionFree')

  if not rospy.has_param('~PublishFrequency'):
   rospy.set_param('~PublishFrequency', 0.01)
  self.PublishFrequency = rospy.get_param('~PublishFrequency')

  if not rospy.has_param('~PredictDistance'):
   rospy.set_param('~PredictDistance', 2)
  self.Predict = rospy.get_param('~PredictDistance')


  self.path = []

  self.commands = Queue.Queue(maxsize = 2)
  
  self.Arrivedplog = False

  self.Arrivedolog = False

  self.locker = Lock()
  
  self.CurrentOdom = None
  
  self.Goals = Queue.LifoQueue(maxsize=0)
  
  self.LastSpeed = Twist()
  
  self.Hold = False
  
  self.ArrivedGoal = False
  
  self.CurrentGoal = None
  
 def LogCB(self, e):
  #with self.locker:
  self.Arrivedplog = True
  self.Arrivedolog = True
  self.CurrentPubGoal = self.CurrentGoal
  print 'self.Hold', self.Hold
  if self.Hold:
   if self.ArrivedGoal:
    #self.Goals.get()
    rospy.loginfo('ArrivedGoal: restore original goal')
    if self.Goals.qsize > 0:
     rospy.loginfo('restore original goal')
     rospy.sleep(0.1)
     #self.PubGoal(self.Goals.get())
     self.Hold = False
     self.ArrivedGoal = False
     self.CurrentPubGoal = self.Goals.get()
     print 'self.Goals.get()\n: ', self.CurrentPubGoal, '\n'
    if self.CurrentPubGoal != None:
     self.PubGoal(self.CurrentPubGoal)
  
     
 def PublishCB(self, event):
  #with self.locker:   
  cmd_vel = rospy.Publisher(self.MotionTopice , Twist, queue_size=1)
  cmd = copy.deepcopy(self.commands.get())
  print 'PublishCB cmd: ' ,cmd
  
  if round(cmd.linear.x, 2) != 0.0:
   if abs(cmd.linear.x) > self.MaxLinearSP:
    cmd.linear.x = self.MaxLinearSP * (cmd.linear.x / abs(cmd.linear.x))
   if abs(cmd.linear.x) < self.MinLinearSP:
    cmd.linear.x = self.MinLinearSP * (cmd.linear.x / abs(cmd.linear.x))
  if round(cmd.angular.z) != 0.0:
   if abs(cmd.angular.z) > self.MaxAngularSP:
    cmd.angular.z = self.MaxAngularSP * (cmd.angular.z / abs(cmd.angular.z))
   if abs(cmd.angular.z) < self.MinAngularSP:
    cmd.angular.z = self.MinAngularSP * (cmd.angular.z / abs(cmd.angular.z))
   
  self.LastSpeed = cmd
  cmd_vel.publish(cmd)


 def GoalCB(self, goal):
  #with self.locker:
  self.CurrentGoal = PointStamped()
  self.CurrentGoal.point = goal.pose.position
  self.CurrentGoal.header.seq = goal.header.seq
  self.CurrentGoal.header.frame_id = goal.header.frame_id


 def PlanCB(self, PlanPath):
  #with self.locker:
  self.path = []
  #self.path = copy.deepcopy(PlanPath.poses)
  
  # check if plan start from current position if yes copy path, otherwise set new goal
  if self.PositionCheck(PlanPath.poses[0], self.CurrentOdom): 
   self.path = copy.deepcopy(PlanPath.poses)
  else:
   if len(PlanPath.poses) > 0:
    new_goal = PointStamped()
    OriGoal = PointStamped()
    new_goal.point = PlanPath.poses[0].pose.position
    new_goal.header.seq = PlanPath.header.seq
    new_goal.header.frame_id = 'map'
    rospy.loginfo('publish new goal')
    #print len(PlanPath.poses)
    self.PubGoal(new_goal)
    #self.Goals.put(new_goal)
    
    if self.CurrentGoal != None:
     #OriGoal.point = self.CurrentGoal.pose.position
     #OriGoal.header.seq = self.CurrentGoal.header.seq
     #OriGoal.header.frame_id = self.CurrentGoal.header.frame_id
     OriGoal = copy.deepcopy(self.CurrentGoal)
     self.Goals.put(OriGoal)
    else:
     OriGoal.point = PlanPath.poses[-1].pose.position
     OriGoal.header.seq = PlanPath.header.seq
     OriGoal.header.frame_id = 'map'
     self.PubGoal(OriGoal)
     #self.Goals.put(OriGoal)
   else:
    rospy.loginfo('No plan coming')
    
   self.Hold = True

   
 def PubGoal(self, new_goal):
  pub_goal = rospy.Publisher("/clicked_point", PointStamped, queue_size=1)
  pub_goal.publish(new_goal)

 
 def PositionCheck(self, PathStartFrom, CurrentOdom):
  if  CurrentOdom == None:
   return False
  else:
   x = PathStartFrom.pose.position.x - CurrentOdom.position.x
   y = PathStartFrom.pose.position.y - CurrentOdom.position.y
   z = PathStartFrom.pose.position.z - CurrentOdom.position.z
   distance = numpy.sqrt(x**2 + y**2 + z**2)
   if distance > 5 * self.PathBias:
    return False
   else:
    return True
   
   
 def OdomCB(self, odom):
  with self.locker:
   self.CurrentOdom = odom
   self.num = 10
   cmd = Twist()
   if self.path != []:
    path = copy.deepcopy(self.path)
    if len(self.path) > self.num :
     cmd = self.DiffControl(odom, path[self.num].pose, path, cmd) 
    else: 
     # situation of len(self.path) < self.num
     if not self.ArrivedPosition(odom, path):
      if self.Arrivedplog:
       self.Arrivedplog = False
       #rospy.loginfo('OdomCB: robot not in goal position ')
      cmd = self.GTP(odom, path[-1].pose, len(path), cmd) 
     else:
      #rospy.loginfo('OdomCB: robot in goal position ')
      cmd = self.GetOrientation(odom, path)
     
    if not cmd == Twist():
     self.commands.put(cmd)
     


 def GetCommand(self, GoalAngle, OdomAngle):

  cmdtwist = None
  OdomToC = None
  
  #如果goal和当前朝向相同  
  if GoalAngle * OdomAngle >= 0:
   CrossFire = False
   #rospy.loginfo('GetCommand: reg. as same orientation')
   OdomToC = GoalAngle - OdomAngle
    
  #如果不同边（存在符号更变）：只需要以最快速度过界，从而达到同边即可
  else:
   CrossFire = True
   GoalToCPP = numpy.pi - abs(GoalAngle)
   OdomToCPP = numpy.pi - abs(OdomAngle)

   GoalToCPO = abs(GoalAngle)
   OdomToCPO = abs(OdomAngle)
   
   # 不同边,判断临界线
   # goal 临界线
   if GoalToCPP < GoalToCPO:
    GCriticalLine = numpy.pi
   
   else:
    GCriticalLine = 0
   # Odom 临界线   
   if OdomToCPP < GoalToCPO:
    OCriticalLine = numpy.pi
   else:
    OCriticalLine = 0
    
   # 不同边,同临界线
   if OCriticalLine == GCriticalLine:
    #rospy.loginfo('GetCommand: reg as same critical line')
    # 不同边, pi 临界线 临界角
    if OCriticalLine == numpy.pi:
     #rospy.loginfo('GetCommand: changing line in pi')
     if GoalAngle >= 0:
      #rospy.loginfo('GetCommand: goal upon line in pi')
      OdomToC = -(abs(GoalAngle) + abs(OdomAngle))
     else:
      #rospy.loginfo('GetCommand: goal under line in pi')
      OdomToC = (abs(GoalAngle) + abs(OdomAngle))
           
    # 不同边,0 临界线 临界角
    elif OCriticalLine == 0: #
     #rospy.loginfo('GetCommand: changing line in 0')
     if GoalAngle >= 0:
      #rospy.loginfo('GetCommand: goal upon line in 0')
      OdomToC = (abs(GoalAngle) + abs(OdomAngle))
     else:
      #rospy.loginfo('GetCommand: goal under line in 0')
      OdomToC = -(abs(GoalAngle) + abs(OdomAngle))
    else:
     #rospy.loginfo('GetCommand: differ changing point in ???')
     pass
     
   # 不同边, 不同临界线
   else:
    #rospy.loginfo('GetCommand: reg as differ critical line')
    # 不同边,  pi 临界线 
    if OdomToCPP + GoalToCPP < OdomToCPO + GoalToCPO:
     #rospy.loginfo('GetCommand: differ changing point in pi')

     if OdomAngle > 0: 
      OdomToC = (numpy.pi - OdomAngle)
     else:
      OdomToC = (-numpy.pi - OdomAngle)
      
     if abs(OdomToC) >= self.MaxAngularSP:
      OdomToC = self.MaxAngularSP * (OdomToC/abs(OdomToC))
     else:
      OdomToC = self.MaxAngularSP * (OdomToC/abs(OdomToC)) / 2
    # 不同边, 0 临界线
    elif OdomToCPP + GoalToCPP >= OdomToCPO + GoalToCPO:
     #rospy.loginfo('GetCommand: differ changing point in 0')
     OdomToC = (0 - OdomAngle)
     
     if abs(OdomToC) >= self.MaxAngularSP:
      OdomToC = self.MaxAngularSP * (OdomToC/abs(OdomToC))

    else:
     #rospy.loginfo('GetCommand: differ changing point in ???')
     pass
     
   # 转角速度生成
  if self.MinAngularSP < abs(OdomToC) < self.AngularBias:
   cmdtwist = OdomToC
  elif abs(OdomToC) <= self.MinAngularSP:
   cmdtwist = OdomToC * 2
  else:    
   cmdtwist = self.MaxAngularSP * (OdomToC/abs(OdomToC))
    
  #rospy.loginfo('GetCommand: establishing AngularSP: ' + str(cmdtwist) + 'max MaxAngularSP: ' + str(self.MaxAngularSP) + ' ' + str(OdomToC))
   
  return (cmdtwist, CrossFire)
 
  

 def DiffControl(self, odom, goal, path, cmd):
  
  (angular_drift, x_drift, y_drift) = self.Drifts(goal, odom)
  
  GoalAngle = angular_drift
  OdomAngle = CVlib.GetAngle(odom.orientation)

  (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle)
  linear = numpy.sqrt(x_drift**2 + y_drift**2)
  boost = self.FrontClean(odom, path)
  
  # 是当前坐标否在误差允许之内
  if linear > self.PathBias:
   if abs(cmdtwist) >= self.AngularBias:
    #rospy.loginfo('DiffControl: AngularBias: in position twist')
    cmd.angular.z = cmdtwist
     
   elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
    #rospy.loginfo('DiffControl: AngularBias: small circle')
    cmd.angular.z = cmdtwist
    if linear < self.MaxLinearSP:
     cmd.linear.x = linear 
    else:
     cmd.linear.x = self.MaxLinearSP

   elif self.AngularFree/2 < abs(cmdtwist) <= self.AngularFree :
    #if CrossFire:
     #rospy.loginfo('DiffControl: AngularFree: in position twist')
     #cmd.angular.z = cmdtwist
    #else:
    #rospy.loginfo('DiffControl: AngularFree: forward')
    cmd.angular.z = cmdtwist
    if linear < self.MaxLinearSP:
     cmd.linear.x = linear 
    else:
     cmd.linear.x = self.MaxLinearSP
       
   else:
    cmd.angular.z = cmdtwist
     
    if boost:
     #rospy.loginfo('DiffControl: FrontClear MAX speed moving')
     cmd = self.Acceleration(self.LastSpeed, cmd) #self.MaxLinearSP
    else:
     #rospy.loginfo('DiffControl: Small circle turning')
     if linear < self.MaxLinearSP:
      cmd.linear.x = linear 
     else:
      cmd.linear.x = self.MaxLinearSP
     
  else:
   #rospy.loginfo('DiffControl: plan circle move directly to pose')
   pose = path[self.num].pose
   cmd = self.cmd_gen(cmdtwist, CrossFire, linear, cmd)
   
  return cmd
  
  
 def Acceleration(self, speed, cmd):
  if speed < self.MaxLinearSP:
   cmd.linear.x = speed.linear.x + 0.01
  else :
   cmd.linear.x = self.MaxLinearSP
  return cmd
  
  
  
 def cmd_gen(self, cmdtwist, CrossFire, linear, cmd):
  if abs(cmdtwist) >= self.AngularBias:
   #rospy.loginfo('cmd_gen: AngularBias: in position twist')
   cmd.angular.z = cmdtwist
     
  elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
   #rospy.loginfo('cmd_gen: AngularBias: small circle')
   cmd.angular.z = cmdtwist
   cmd.linear.x = linear 

  else: # abs(cmdtwist) <= self.AngularFree 
   if CrossFire:
    #rospy.loginfo('cmd_gen: AngularFree: in position twist')
    cmd.angular.z = cmdtwist
   else:
    #rospy.loginfo('cmd_gen: AngularFree: forward')
    #cmd.angular.z = cmdtwist
    cmd.linear.x = linear
    
  return cmd
  
  
 def GTP(self, odom, pose, PathLength, cmd):
  
  (angular_drift, x_drift, y_drift) = self.Drifts(pose, odom)
  
  linear = numpy.sqrt(x_drift**2 + y_drift**2)

  if linear > self.PositionFree:
  
   GoalAngle = angular_drift
   OdomAngle = CVlib.GetAngle(odom.orientation)

   (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle)
   
   cmd = self.cmd_gen(cmdtwist, CrossFire, linear, cmd)
  
  else:  
   #rospy.loginfo('GTP: plan circle')
   
   odom_angle = CVlib.GetAngle(odom.orientation)
   goal_angle = CVlib.GetAngle(pose.orientation)
    
   cmd = self.IPT(odom_angle, goal_angle, cmd) 

  return cmd
  
  

 def GetOrientation(self, odom, path):
  cmd = Twist()
  odom_angle = CVlib.GetAngle(odom.orientation)
  goal_angle = CVlib.GetAngle(path[-1].pose.orientation)
  if not self.ArrivedOrientation(odom_angle, goal_angle):
   cmd = self.IPT(odom_angle, goal_angle, cmd) 
   return cmd
  else:
   return cmd


 def IPT(self, OdomAngle, GoalAngle, cmd):

  (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle)

  #rospy.loginfo('IPT: cmdtwist：' + str(cmdtwist)+ '  AngularFree: ' + str(self.AngularFree))
  if abs(cmdtwist) > self.AngularFree:
   #rospy.loginfo('IPT: in position twist')
   cmd.angular.z = cmdtwist
  else:
   #rospy.loginfo('IPT: error less than threld')
   pass
  return cmd


 def ArrivedOrientation(self, odom_angle, goal_angle):
  #同边
  if odom_angle * goal_angle > 0:
   if abs(odom_angle - goal_angle) < self.AngularFree:
    if self.Arrivedolog:
     self.Arrivedolog = False
     rospy.loginfo('ArrivedOrientation: robot in goal orientation1 ')
     self.ArrivedGoal = True
     self.define()
    return True
   else:
    return False
  #不同边
  else:
   if abs(odom_angle) > numpy.pi/2:
    Arrived = 2 * numpy.pi - (abs(odom_angle) + abs(goal_angle))
   else: 
    Arrived = (abs(odom_angle) + abs(goal_angle))
   #print 'ArrivedOrientation: ', Arrived
   
   if Arrived < self.AngularFree:
    if self.Arrivedplog:
     self.Arrivedplog = False
     rospy.loginfo('ArrivedOrientation: robot in goal orientation2 ')
     self.ArrivedGoal = True
     self.define()
    return True
   else:
    return False
    
        
 def ArrivedPosition(self, odom, path):
  x = odom.position.x
  y = odom.position.y
  #print abs(x - path[-1].pose.position.x), abs(y - path[-1].pose.position.y)
  if numpy.sqrt(abs(x - path[-1].pose.position.x)**2 + abs(y - path[-1].pose.position.y)**2) < self.PositionFree:
   if self.Arrivedplog:
    self.Arrivedplog = False
    rospy.loginfo('ArrivedPosition: robot in goal position ')
   return True
  else:
   return False
  
  
 def FrontClean(self, odom, path):
  Predict_Distance = self.num * self.Predict
  Forward_Distance = self.num
  if len(path) >= (self.num + Predict_Distance):
   return self.FrontMAX(Predict_Distance, Forward_Distance, odom, path)
  else:
   return False
 
   
 def FrontMAX(self, Predict_Distance, Forward_Distance, odom, path):

  FrontLine = CVlib.SLF()
  
  Front1 = copy.deepcopy(path[: Predict_Distance])
  (Line1, CoefficientA1, CoefficientB1, CoefficientC1) = FrontLine.OLS(Front1) 

  Coe1 = [CoefficientA1, CoefficientB1]
 
  Orientation = odom.orientation
  SimilarLines = FrontLine.Orientation_line_com(Orientation, Coe1)
  
  if SimilarLines:
   return True
  else:
   return False



 def Drifts(self, goal, odom): 
 
  x_drift = goal.position.x - odom.position.x
  y_drift = goal.position.y - odom.position.y 
  angular_drift = numpy.arcsin(y_drift / numpy.sqrt(x_drift**2 + y_drift**2))
  
  if x_drift > 0 and y_drift < 0:
   angular_drift = angular_drift
   
  if x_drift > 0 and y_drift > 0:
   angular_drift = angular_drift
   
  if x_drift < 0 and y_drift < 0:
   angular_drift = -angular_drift - numpy.pi
   
  if x_drift < 0 and y_drift > 0:
   angular_drift = numpy.pi - angular_drift
   
  return (angular_drift, x_drift, y_drift)
  


 
if __name__=='__main__':

 rospy.init_node('BaseController_X')
 
 #try:
 
 rospy.loginfo( "initialization system")
 BaseController()
 ClearParams()
 
 #except rospy.ROSInterruptException:
 
 rospy.loginfo("node terminated.")


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
  rospy.delete_param('~PlanTopic')
  rospy.delete_param('~OdomTopic')
  rospy.delete_param('~MotionTopice')
  rospy.delete_param('~PathBias')
  rospy.delete_param('~MaxLinearSP')
  rospy.delete_param('~MaxAngularSP')
  rospy.delete_param('~AngularBias')
  rospy.delete_param('~AngularFree')
  rospy.delete_param('~PositionFree')
  rospy.delete_param('~PublishFrequency')
  
class BaseController:
 def __init__(self):
  self.define()
  rospy.Subscriber('%s'%self.OdomTopic, Pose, self.OdomCB)
  rospy.Subscriber('%s'%self.PlanTopic, Path, self.PlanCB)
  rospy.Timer(rospy.Duration(self.PublishFrequency), self.PublishCB)
  rospy.Timer(rospy.Duration(self.PublishFrequency*50), self.LogCB)
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
   rospy.set_param('~MaxLinearSP', 0.3)
  self.MaxLinearSP = rospy.get_param('~MaxLinearSP')
   
  if not rospy.has_param('~MaxAngularSP'):
   rospy.set_param('~MaxAngularSP', 0.4)
  self.MaxAngularSP = rospy.get_param('~MaxAngularSP')

  if not rospy.has_param('~AngularBias'):
   rospy.set_param('~AngularBias', 0.3)
  self.AngularBias = rospy.get_param('~AngularBias')

  if not rospy.has_param('~AngularFree'):
   rospy.set_param('~AngularFree', 0.1745)
  self.AngularFree = rospy.get_param('~AngularFree')

  if not rospy.has_param('~PositionFree'):
   rospy.set_param('~PositionFree', 0.02)
  self.PositionFree = rospy.get_param('~PositionFree')

  if not rospy.has_param('~PublishFrequency'):
   rospy.set_param('~PublishFrequency', 0.1)
  self.PublishFrequency = rospy.get_param('~PublishFrequency')


  # topics
  self.cmd_vel = rospy.Publisher(self.MotionTopice , Twist, queue_size=1)

  self.path = []

  self.commands = Queue.Queue(maxsize = 2)
  
  self.Arrivedplog = False

  self.Arrivedolog = False

  self.locker = Lock()
  
  self.CurrentOdom = None
  
  self.Goals = Queue.LifoQueue(maxsize=0)
  
  
 def LogCB(self, e):
  #with self.locker:
  self.Arrivedplog = True
  self.Arrivedolog = True
  
  
 def PublishCB(self, event):
  #with self.locker:
  cmd = self.commands.get()
  if cmd != Twist():
   self.cmd_vel.publish(cmd)
  else:
   pass


 def GoalCB(self, goal):
  #with self.locker:
  self.CurrentGoal = goal


 def PlanCB(self, PlanPath):
  #with self.locker:
  self.path = []
  self.path = copy.deepcopy(PlanPath.poses)
  
  """# check if plan start from current position if yes copy path, otherwise set new goal
  if self.StartPositionCheck(PlanPath.poses[0], self.CurrentOdom): 
   self.path = copy.deepcopy(PlanPath.poses)
   self.Goals.get()
  else:
   new_goal = PointStamped()
   new_goal.point = self.CurrentGoal.pose.position
   new_goal.header.seq = self.CurrentGoal.header.seq
   new_goal.header.frame_id = self.CurrentGoal.header.frame_id
   self.Goals.put(self.CurrentGoal)
   self.PubGoal(new_goal)"""

   
   
 def PubGoal(self, new_goal):
  pub_goal = rospy.Publisher("/clicked_point", PointStamped, queue_size=1)
  pub_goal.publish(new_goal)



 
 def StartPositionCheck(self, PathStartFrom, CurrentOdom):
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
   #print '\n'
   self.num = 10
   #print 'path: ', len(self.path), self.num
   cmd = Twist()
   if self.path != []:
    path = copy.deepcopy(self.path)
    if len(self.path) > self.num :
     cmd = self.DiffControl(odom, path[self.num].pose, path) 
    else:
     #print 'ArrivedPosition: ', self.ArrivedPosition(odom, path)
     if not self.ArrivedPosition(odom, path):
      if self.Arrivedplog:
       self.Arrivedplog = False
       rospy.loginfo('OdomCB: robot not in goal position ')
      cmd = self.GTP(odom, path[-1].pose, path) 
     else:
      rospy.loginfo('OdomCB: robot in goal position ')
      cmd = self.GetOrientation(odom, path)
      
  if not cmd == Twist():
   self.commands.put(cmd)
  

 def GetOrientation(self, odom, path):
  cmd = Twist()
  if not self.ArrivedOrientation(odom, path):
   cmd = self.IPT(odom, cmd, self.goal) 
   return cmd
  else:
   return cmd


 def GTP(self, odom, pose, path):
  cmd = Twist()
  CrossFire = False
  
  (angular_drift, x_drift, y_drift) = self.Drifts(pose, odom)

  if abs(x_drift) > self.PositionFree or abs(y_drift) > self.PositionFree or (abs(x_drift)**2 + abs(y_drift)**2) > self.PositionFree:
  
   GoalAngle = angular_drift
   OdomAngle = CVlib.GetAngle(odom.orientation)

   (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle, CrossFire)
  
   if abs(cmdtwist) >= self.AngularBias:
    #rospy.loginfo('GTP: AngularBias: in position twist')
    cmd.angular.z = cmdtwist
     
   elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
    linear = numpy.sqrt(x_drift**2 + y_drift**2)
    #rospy.loginfo('GTP: AngularBias: small circle')
    cmd.angular.z = cmdtwist
    cmd.linear.x = linear 

   else: # abs(cmdtwist) <= self.AngularFree 
    if CrossFire:
     #rospy.loginfo('GTP: AngularFree: in position twist')
     cmd.angular.z = cmdtwist
    else:
     linear = numpy.sqrt(x_drift**2 + y_drift**2)
     #rospy.loginfo('GTP: AngularFree: forward')
     cmd.angular.z = cmdtwist
     cmd.linear.x = linear
  
  else:  
   if self.num > len(path) > 0:
    rospy.loginfo('GTP: plan circle')
    goal = CVlib.GetAngle(path[-1].pose.orientation)
    cmd = self.IPT(odom, cmd, goal) 
   else:
    GoalAngle = angular_drift
    OdomAngle = CVlib.GetAngle(odom.orientation)
    (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle, CrossFire)
    if abs(cmdtwist) >= self.AngularBias:
     #rospy.loginfo('GTP: AngularBias: in position twist')
     cmd.angular.z = cmdtwist
     
    elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
     linear = numpy.sqrt(x_drift**2 + y_drift**2)
     #rospy.loginfo('GTP: AngularBias: small circle')
     cmd.angular.z = cmdtwist
     cmd.linear.x = linear 

    else: # abs(cmdtwist) <= self.AngularFree 
     if CrossFire:
      #rospy.loginfo('GTP: AngularFree: in position twist')
      cmd.angular.z = cmdtwist
     else:
      linear = numpy.sqrt(x_drift**2 + y_drift**2)
      #rospy.loginfo('GTP: AngularFree: forward')
      cmd.angular.z = cmdtwist
      cmd.linear.x = linear

  return cmd


 def IPT(self, odom, cmd, goal):
  CrossFire = False

  GoalAngle = goal
  OdomAngle = CVlib.GetAngle(odom.orientation)

  (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle, CrossFire)

  #rospy.loginfo('IPT: cmdtwist：' + str(cmdtwist)+ '  AngularFree: ' + str(self.AngularFree))

  if abs(cmdtwist) > self.AngularFree:
   rospy.loginfo('IPT: in position twist')
   cmd.angular.z = cmdtwist
  else:
   rospy.loginfo('IPT: error less than threld')
  return cmd



 def ArrivedOrientation(self, odom, path):
  angle = CVlib.GetAngle(odom.orientation)
  self.goal = CVlib.GetAngle(path[-1].pose.orientation)
  #同边
  if angle * self.goal > 0:
   if abs(angle - self.goal) < self.AngularFree:
    if self.Arrivedolog:
     self.Arrivedolog = False
     rospy.loginfo('ArrivedOrientation: robot in goal orientation ')
    return True
   else:
    return False
  #不同边
  else:
   if abs(angle) > numpy.pi/2:
    Arrived = 2 * numpy.pi - (abs(angle) + abs(self.goal))
   else: 
    Arrived = (abs(angle) + abs(self.goal))
   #print 'ArrivedOrientation: ', Arrived
   
   if Arrived < self.AngularFree:
    if self.Arrivedplog:
     self.Arrivedplog = False
     rospy.loginfo('ArrivedOrientation: robot in goal orientation ')
    return True
   else:
    return False
    
    
 def ArrivedPosition(self, odom, path):
  x = odom.position.x
  y = odom.position.y
  #print abs(x - path[-1].pose.position.x), abs(y - path[-1].pose.position.y)
  if abs(x - path[-1].pose.position.x) < self.PositionFree and abs(y - path[-1].pose.position.y) < self.PositionFree and numpy.sqrt(abs(x - path[-1].pose.position.x)**2 + abs(y - path[-1].pose.position.y)**2) < self.PositionFree:
   if self.Arrivedplog:
    self.Arrivedplog = False
    rospy.loginfo('ArrivedPosition: robot in goal position ')
   return True
  else:
   return False
  
  
 def FrontClean(self, odom, path):
  Predict_Distance = self.num*2
  Forward_Distance = self.num
  if len(path) >= (self.num + Predict_Distance):
   return self.FrontMAX(Predict_Distance, Forward_Distance, odom, path)
  else:
   return False
 
   
 def FrontMAX(self, Predict_Distance, Forward_Distance, odom, path):

  FrontLine = CVlib.SLF()
  
  Front1 = copy.deepcopy(path[: Predict_Distance])
  (Line1, CoefficientA1, CoefficientB1, CoefficientC1) = FrontLine.OLS(Front1) 
  
  #Front2 = copy.deepcopy(path[: Forward_Distance])
  #(Line2, CoefficientA2, CoefficientB2, CoefficientC2) = FrontLine.OLS(Front2)  
   
  Coe1 = [CoefficientA1, CoefficientB1]
  #Coe2 = [CoefficientA2, CoefficientB2]
  
  #SimilarLines = FrontLine.get_similar_lines(Coe1, Coe2)
  
  #print 'FrontMAX: ', self.num, len(Front1), len(Front2), SimilarLines
  #print 'Line1: ', (Line1, CoefficientA1, CoefficientB1, CoefficientC1)
  #print 'Line2: ', (Line1, CoefficientA2, CoefficientB2, CoefficientC2)
  
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
  
  
 def GoalOrientation(self, theta):
  orientation = Quaternion() 
  
  if -numpy.pi < theta < -numpy.pi*2.0/3.0:
   orientation.z = -numpy.sin(theta/2.0)
   orientation.w = -numpy.cos(theta/2.0)
   
  else:
   orientation.z = numpy.sin(theta/2.0)
   orientation.w = numpy.cos(theta/2.0)
   
  return orientation
    
  
 #def GetAngle(self, quat):
  #rot = PyKDL.Rotation.Quaternion(quat.x, quat.y, quat.z, quat.w)
  #return rot.GetRPY()[2]
  
 
 def GetCommand(self, GoalAngle, OdomAngle, CrossFire):

  cmdtwist = None
  OdomToC = None
  
  #如果goal和当前朝向相同  
  if GoalAngle * OdomAngle >= 0:
   CrossFire = False
   rospy.loginfo('GetCommand: reg. as same orientation')
   OdomToC = (GoalAngle - OdomAngle)
    
  #如果不同边（存在符号更变）：只需要以最快速度过界，从而达到同边即可
  else:
   CrossFire = True
   GoalToCPP = abs(numpy.pi - abs(GoalAngle))
   OdomToCPP = abs(numpy.pi - abs(OdomAngle))

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
    rospy.loginfo('GetCommand: reg as same critical line')
    # 不同边, pi 临界线 临界角
    if OCriticalLine == numpy.pi:
     rospy.loginfo('GetCommand: changing line in pi')
     if GoalAngle >= 0:
      rospy.loginfo('GetCommand: goal upon line in pi')
      OdomToC = -(abs(GoalAngle) + abs(OdomAngle))
      #OdomToC = (numpy.pi - abs(OdomAngle) )
     else:
      rospy.loginfo('GetCommand: goal under line in pi')
      OdomToC = (abs(GoalAngle) + abs(OdomAngle))
      #OdomToC = -(numpy.pi - abs(OdomAngle))
           
    # 不同边,0 临界线 临界角
    elif OCriticalLine == 0: #
     rospy.loginfo('GetCommand: changing line in 0')
     if GoalAngle >= 0:
      rospy.loginfo('GetCommand: goal upon line in 0')
      OdomToC = (abs(GoalAngle) + abs(OdomAngle))
      #OdomToC = (0 - abs(OdomAngle))
     else:
      rospy.loginfo('GetCommand: goal under line in 0')
      OdomToC = -(abs(GoalAngle) + abs(OdomAngle))
      #OdomToC = -(0 - abs(OdomAngle))
    else:
     rospy.loginfo('GetCommand: differ changing point in ???')
     pass
     
   # 不同边, 不同临界线
   else:
    rospy.loginfo('GetCommand: reg as differ critical line')
    # 不同边,  pi 临界线 
    if OdomToCPP + GoalToCPP < OdomToCPO + GoalToCPO:
     rospy.loginfo('GetCommand: differ changing point in pi')
     #if OCriticalLine == numpy.pi and GCriticalLine == 0:
      #OdomToC = (OdomToCPP + OdomAngle)
     #if OCriticalLine == 0 and GCriticalLine == numpy.pi:
      #OdomToC = -(OdomToCPP + OdomAngle)
     if OdomAngle > 0: 
      OdomToC = (numpy.pi - OdomAngle)
     else:
      OdomToC = (-numpy.pi - OdomAngle)
      
     if abs(OdomToC) <= self.MaxAngularSP:
      OdomToC = self.MaxAngularSP * (OdomToC/abs(OdomToC))

    # 不同边, 0 临界线
    elif OdomToCPP + GoalToCPP >= OdomToCPO + GoalToCPO:
     rospy.loginfo('GetCommand: differ changing point in 0')
     #if OCriticalLine == numpy.pi and GCriticalLine == 0:
      #OdomToC = -(OdomToCPO + OdomAngle)
     #if OCriticalLine == 0 and GCriticalLine == numpy.pi:
      #OdomToC = (OdomToCPO + OdomAngle)
     OdomToC = (0 - OdomAngle)
     
     if abs(OdomToC) <= self.MaxAngularSP:
      OdomToC = self.MaxAngularSP * (OdomToC/abs(OdomToC))

    else:
     rospy.loginfo('GetCommand: differ changing point in ???')
     pass
     
   # 转角速度生成
  if 0.05 < abs(OdomToC) < self.AngularBias:
   cmdtwist = OdomToC

  elif abs(OdomToC) <= 0.05:
   cmdtwist = OdomToC * 2
    
  else:    
   cmdtwist = abs(self.MaxAngularSP) * (OdomToC/abs(OdomToC))
    
  #rospy.loginfo('GetCommand: establishing AngularSP: ' + str(cmdtwist) + 'max MaxAngularSP: ' + str(self.MaxAngularSP) + ' ' + str(OdomToC))
   
  return (cmdtwist, CrossFire)
 
 
 
 def DiffControl(self, odom, goal, path):
  cmd = Twist()
  CrossFire = False
  
  (angular_drift, x_drift, y_drift) = self.Drifts(goal, odom)
  
  #Gorientation = self.GoalOrientation(angular_drift)

  GoalAngle = angular_drift
  OdomAngle = CVlib.GetAngle(odom.orientation)

  (cmdtwist, CrossFire) = self.GetCommand(GoalAngle, OdomAngle, CrossFire)

  # 是当前坐标否在误差允许之内
  if abs(x_drift) > self.PathBias or abs(y_drift) > self.PathBias or numpy.sqrt(abs(x_drift)**2 + abs(y_drift)**2) > self.PathBias:
   if abs(cmdtwist) >= self.AngularBias:
    rospy.loginfo('DiffControl: AngularBias: in position twist')
    cmd.angular.z = cmdtwist #self.MaxAngularSP
     
   elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
    linear = numpy.sqrt(x_drift**2 + y_drift**2)
    rospy.loginfo('DiffControl: AngularBias: small circle')
    cmd.angular.z = cmdtwist
    cmd.linear.x = linear 

   elif self.AngularFree/2 < abs(cmdtwist) <= self.AngularFree :
    if CrossFire:
     rospy.loginfo('DiffControl: AngularFree: in position twist')
     cmd.angular.z = cmdtwist
    else:
     linear = numpy.sqrt(x_drift**2 + y_drift**2)
     rospy.loginfo('DiffControl: AngularFree: forward')
     cmd.angular.z = cmdtwist
     cmd.linear.x = linear
       
   else:
    if CrossFire:
     rospy.loginfo('DiffControl: AngularFree: in position twist')
     cmd.angular.z = cmdtwist
    else:
     rospy.loginfo('DiffControl: AngularFree: forward')
     cmd.angular.z = cmdtwist

    if GoalAngle * OdomAngle >= 0:     
     if self.FrontClean(odom, path):
      rospy.loginfo('#################DiffControl: FrontClear MAX speed moving')
      cmd.linear.x = self.MaxLinearSP
     else:
      rospy.loginfo('#################DiffControl: Small circle turning')
      linear = numpy.sqrt(x_drift**2 + y_drift**2)
      cmd.linear.x = linear
     
  else:
   rospy.loginfo('DiffControl: plan circle')
   pose = path[self.num].pose
   cmd = self.GTP(odom, pose, path) 

  return cmd
 
if __name__=='__main__':

 rospy.init_node('BaseController_X')
 
 #try:
 
 rospy.loginfo( "initialization system")
 BaseController()
 ClearParams()
 
 #except rospy.ROSInterruptException:
 
 rospy.loginfo("node terminated.")


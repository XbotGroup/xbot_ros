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
  #rospy.delete_param('~GoalTolerent')

class BaseController:
 def __init__(self):
  self.define()
  rospy.Subscriber('%s'%self.OdomTopic, Pose, self.OdomCB)
  rospy.Subscriber('%s'%self.PlanTopic, Path, self.PlanCB)
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
   rospy.set_param('~PathBias', 0.01) 
  self.PathBias = rospy.get_param('~PathBias')

  if not rospy.has_param('~MaxLinearSP'):
   rospy.set_param('~MaxLinearSP', 0.5)
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
  
  # topics
  self.cmd_vel = rospy.Publisher(self.MotionTopice , Twist, queue_size=1)

  self.path = []


 def OdomCB(self, odom):
  self.num = 10 #int( 0.2 * len(self.path))
  print 'path: ', len(self.path), self.num
  cmd = Twist()
  if self.path != []:
   if len(self.path) > self.num :
    cmd = self.DiffControl(odom, self.path[self.num].pose) 
   else:
    try:
     cmd = self.DiffControl(odom, self.path[1].pose) 
    except:
     cmd = self.DiffControl(odom, self.path[0].pose) 
  self.cmd_vel.publish(cmd)
   
   
 def PlanCB(self, PlanPath):
  self.path = []
  self.path = PlanPath.poses
  
 def FrontClean(self):
  Front = copy.deepcopy(self.path[self.num:self.num*2])
  Frontx = []
  Fronty = []
  for item in Front:
   Frontx.append(item.pose.position.x)
   Fronty.append(item.pose.position.y)
  Meanx = float(sum(Frontx)) / self.num
  Meany = float(sum(Frontx)) / self.num
  print self.num, len(Frontx)
    
    
    
 def AngularDrift(self, goal, odom): 
 
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
    
  
 def GetAngle(self, quat):
  rot = PyKDL.Rotation.Quaternion(quat.x, quat.y, quat.z, quat.w)
  return rot.GetRPY()[2]
  
 
 def DiffControl(self, odom, goal):
  cmd = Twist()
  CrossFire = False
  
  (angular_drift, x_drift, y_drift) = self.AngularDrift(goal, odom)
  
  Gorientation = self.GoalOrientation(angular_drift)
  linear = numpy.sqrt(x_drift**2 + y_drift**2)

  GoalAngle = self.GetAngle(Gorientation)
  OdomAngle = self.GetAngle(odom.orientation)
  
  #如果goal和当前朝向相同
  if GoalAngle * OdomAngle >= 0:
   cmdtwist = GoalAngle - OdomAngle 
  
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
    rospy.loginfo('reg as same critical line')
    # 不同边, pi 临界线 临界角
    if OCriticalLine == numpy.pi:
     rospy.loginfo('changing line in pi')
     if GoalAngle >= 0:
      rospy.loginfo('goal upon line in pi')
      OdomToC = -abs(abs(GoalAngle) - abs(OdomAngle))
     else:
      rospy.loginfo('goal under line in pi')
      OdomToC = abs(abs(GoalAngle) - abs(OdomAngle))
           
    # 不同边,0 临界线 临界角
    elif OCriticalLine == 0: #
     rospy.loginfo('changing line in 0')
     if GoalAngle >= 0:
      rospy.loginfo('goal upon line in pi')
      OdomToC = abs(abs(GoalAngle) - abs(OdomAngle))
     else:
      rospy.loginfo('goal under line in pi')
      OdomToC = -abs(abs(GoalAngle) - abs(OdomAngle))
    else:
     rospy.loginfo('differ changing point in ???')
    
   # 不同边, 不同临界线
   else:
    rospy.loginfo('reg as differ critical line')
    # 不同边,  pi 临界线 
    if OdomToCPP + GoalToCPP < OdomToCPO + GoalToCPO:
     rospy.loginfo('differ changing point in pi')
     OdomToC = OdomToCPP
    # 不同边, 0 临界线
    elif OdomToCPP + GoalToCPP >= OdomToCPO + GoalToCPO:
     rospy.loginfo('differ changing point in 0')
     OdomToC = OdomToCPO
    else:
     rospy.loginfo('differ changing point in ???')
    
   # 不同边, 过临界线，转角速度
   if abs(OdomToC) <= 2*abs(self.AngularBias):
    cmdtwist = OdomToC + 0.1 * OdomToC/ (abs(OdomToC))  
        
   else:    
    cmdtwist = abs(self.MaxAngularSP) * OdomToC/abs(OdomToC)

  # 是当前坐标否在误差允许之内
  if abs(x_drift) > self.PathBias or abs(y_drift) > self.PathBias:
  
   if abs(cmdtwist) >= self.AngularBias:
    rospy.loginfo('in position twist')
    cmd.angular.z = cmdtwist #self.MaxAngularSP
     
   elif self.AngularFree < abs(cmdtwist) < self.AngularBias:
    rospy.loginfo('small circle')
    cmd.angular.z = cmdtwist
    cmd.linear.x = linear 

   elif self.AngularFree >= abs(cmdtwist):
    if CrossFire:
     rospy.loginfo('in position twist')
     cmd.angular.z = cmdtwist
    else:
     rospy.loginfo('forward')
     cmd.linear.x = linear
     
    #if self.FrontClean():
     #cmd.linear.x = self.MaxLinearSP
    #else:
     #cmd.linear.x = linear
   else:
    pass
    
  else:
   rospy.loginfo('robot in goal position')
   if self.AngularFree < abs(cmdtwist):
    cmd.angular.z = cmdtwist
     
   else:
    rospy.loginfo('robot in goal orientation')

  #print self.CurAngle, self.NexAngel
  #print 'cmdtwist:',cmdtwist, '  linear:', linear
  #print 'self.PathBias:', self.PathBias, ' drifts less then bias: ', (abs(x_drift), abs(y_drift)) > (self.PathBias, self.PathBias) , ' ComparaOrientation: ', self.ComparaOrientation(Gorientation, odom.orientation), ' ReverseOrientation: ', self.ReverseOrientation( Gorientation, odom.orientation)
  #print 'x_drift: ', x_drift, 'y_drift: ', y_drift, 'angular_drift: ', angular_drift
  #print [round(abs(x_drift),3), round(abs(y_drift),3)]
  #print 'DiffControl: \n',cmd
  #return (cmd, [x_drift, y_drift], angular_drift)
  return cmd
 
if __name__=='__main__':

 rospy.init_node('BaseController_X')
 
 #try:
 
 rospy.loginfo( "initialization system")
 BaseController()
 ClearParams()
 
 #except rospy.ROSInterruptException:
 
 rospy.loginfo("node terminated.")


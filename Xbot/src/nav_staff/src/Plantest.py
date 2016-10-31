#!/usr/bin/env python
#coding=utf-8
""" 
底盘移动控制软件

Copyright (c) 2016 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot. 

"""
import rospy
import copy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Path
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
import PyKDL
import numpy
import CVlib

class Plantest():
 def __init__(self):
  self.define()
  rospy.Subscriber('/turtlebot_position_in_map', Pose, self.OdomCB)
  rospy.Subscriber('%s'%self.PlanTopic, Path, self.PlanCB)
  rospy.spin()
  
 def define(self):
  #parameters
   # real
   # /move_base/NavfnROS/plan
   # /move_base/TrajectoryPlannerROS/local_plan
   # /move_base/TrajectoryPlannerROS/global_plan
   # fake
   # /move_base/NavfnROS/plan
   # /move_base/DWAPlannerROS/local_plan
   # /move_base/DWAPlannerROS/global_plan
   
  if not rospy.has_param('~PlanTopic'):
   rospy.set_param('~PlanTopic','/move_base/NavfnROS/plan')
  rospy.set_param('~PlanTopic','/move_base/NavfnROS/plan')
  self.PlanTopic = rospy.get_param('~PlanTopic')

  rospy.loginfo ('subscribe to topic: ' + self.PlanTopic)
  self.path = []

  self.robot = Marker()
  self.robot.header.frame_id = 'map'
  self.robot_pub = rospy.Publisher("/robot_position", Marker ,queue_size=1)
  self.robot_orien_pub = rospy.Publisher("/robot_orientation", Marker ,queue_size=1)
  self.color = ColorRGBA()
  self.scale = Point()
  self.scale.x=0.05
  self.scale.y=0.05
  self.scale.z=0.05
  self.color.r=2.0
  self.color.g=0.0
  self.color.b=0.0
  self.color.a=1.0

 def OdomCB(self, data):
  self.odom = data
  self.robot_orientation = self.visual_test(copy.deepcopy(self.odom), Marker.ARROW, self.color, self.scale)
  self.robot_orien_pub.publish(self.robot_orientation)
  self.current_orientation = data.orientation
  self.a_odom = self.GetAngle(self.odom.orientation)

  
 def Posi_OR_Nag(self, goal, odom):
  PredictSpeed = -1
  self.OdoAngle = self.GetAngle(odom)
  self.GoaAngle = self.GetAngle(goal)
  self.CurAngle = abs(self.GoaAngle) - abs(self.OdoAngle)
  self.NexAngel = self.GoaAngle - self.OdoAngle + PredictSpeed
  if self.CurAngle > self.NexAngel:
   return PredictSpeed
  else:
   return -PredictSpeed
  
 def GetAngle(self, quat):
  rot = PyKDL.Rotation.Quaternion(quat.x, quat.y, quat.z, quat.w)
  return rot.GetRPY()[2]


 def angular_drift(self, goal, odom):
  x_drift = goal.position.x - odom.position.x
  y_drift = goal.position.y - odom.position.y 
  
  AngularDrift = numpy.arcsin(y_drift / numpy.sqrt(x_drift**2 + y_drift**2))
 
  #print '####################### angular_drift before: ', AngularDrift
  if x_drift > 0 and y_drift < 0:
   AngularDrift = AngularDrift
  if x_drift > 0 and y_drift > 0:
   AngularDrift = AngularDrift
  if x_drift < 0 and y_drift < 0:
   AngularDrift = -AngularDrift - numpy.pi
  if x_drift < 0 and y_drift > 0:
   AngularDrift = numpy.pi - AngularDrift
  #print '####################### AngularDrift after: ', AngularDrift
  return (AngularDrift, x_drift, y_drift)
  
  
  
 def goal_orientation(self, theta):
  orientation = Quaternion() 
  if -numpy.pi < theta < -numpy.pi*2.0/3.0:
   print 'reverse orientation'
   orientation.z = -numpy.sin(theta/2.0)
   orientation.w = -numpy.cos(theta/2.0)
  else:
   orientation.z = numpy.sin(theta/2.0)
   orientation.w = numpy.cos(theta/2.0)
  return orientation
  
  
  
 def PlanCB(self, PlanPath):
  print '############/\n', PlanPath.poses[0]
  self.path = []
  self.path = copy.deepcopy(PlanPath.poses)
  self.num = 10 
  if len(self.path) > self.num:#int( 0.2 * len(self.path))
   self.path[self.num].pose.position.z = 2
   
   self.PlotLines(PlanPath.poses, self.num) 

   self.robot = self.visual_test([self.path[self.num].pose.position, self.odom.position], Marker.POINTS, [copy.deepcopy(self.color),copy.deepcopy(self.color)], self.scale)
   
   self.robot_pub.publish(self.robot)
     
   (AngularDrift, x_drift, y_drift) = self.angular_drift(self.path[self.num].pose, self.odom)
     
   GoalOrientation = self.goal_orientation(AngularDrift)
       
   self.Posi_OR_Nag(copy.deepcopy(GoalOrientation), copy.deepcopy(self.odom.orientation))
     
   #print self.path[-1]
   #print 'CurAngle:', self.CurAngle*(180/numpy.pi), ' odom angle - goal angle = %s - %s: '%(self.OdoAngle*(180/numpy.pi), self.GoaAngle*(180/numpy.pi))
   #print 'subscribe to topic: ', self.PlanTopic, 'len: ', len(self.path)
   #print 'path[0]\n', self.path[0].pose.position
   #print 'path[%s]\n'%self.num, self.path[self.num].pose.position
   #print 'odom\n', self.odom.position
   #print 'AngularDrift: ', AngularDrift * (180 / numpy.pi),  ' x_drift: ', x_drift, ' y_drift: ', y_drift
   #print '\ncurrent_orientation :\n', self.current_orientation
   #print 'goal_orientation:\n', GoalOrientation

  else:
   # plan size less len 2
   self.path[0].pose.position.z = 2
   
   self.robot = self.visual_test([self.path[0].pose.position, self.odom.position], Marker.POINTS, [copy.deepcopy(self.color),copy.deepcopy(self.color)], self.scale)
   
   self.robot_pub.publish(self.robot)
 
   (angular_drift, x_drift, y_drift) = self.angular_drift(self.path[0].pose, self.odom)

   GoalOrientation = self.goal_orientation(angular_drift)

   self.Posi_OR_Nag(copy.deepcopy(GoalOrientation), copy.deepcopy(self.odom.orientation))

   
   #print 'subscribe to topic: ', self.PlanTopic, 'len: ', len(self.path), '\npath[0]\n', self.path[0].pose.position, '\npath[1]\n', self.path[1].pose.position, '\nodom\n', self.odom.position
   #print 'current_orientation :\n', self.current_orientation
   #print 'angular_drift:\n', angular_drift
   #print 'goal_orientation:\n', GoalOrientation 
  
  self.StraightLine(self.num)

 def StraightLine(self, num):
  Front = copy.deepcopy(self.path[:num*2])
  FrontLine = CVlib.SLF()
  result = FrontLine.OLS(Front)
  
  print 'StraightLine length: ', num, 'path length: ', len(self.path)
  #print result
  
  if len(self.path) < 2*num:
   pass
  else:
   blue = ColorRGBA()
   blue.b =1
   blue.a =1
    
   point_marker = Marker()
   point_marker.header.frame_id = '/map'
   point_marker.header.stamp = rospy.Time.now()
   point_marker.ns = ''
   point_marker.action = Marker.ADD
   
   point_marker.id = 0
   point_marker.type = Marker.POINTS
   point_marker.scale.x =  0.05
   point_marker.scale.y =  0.05
   
   for i in range(num):
    point_marker.points.append(self.path[num+i].pose.position)
    point_marker.colors.append(blue)
    
   point_marker.lifetime=rospy.Duration(0.5)
   line_pub = rospy.Publisher("/straight_line", Marker ,queue_size=1)
   line_pub.publish(point_marker)
   
   
 def visual_test(self,data,Type,color,scale):
  if Type == Marker.POINTS:
   point_marker=Marker()
   point_marker.header.frame_id='/map'
   point_marker.header.stamp=rospy.Time.now()
   point_marker.ns='plan_test'
   point_marker.action=Marker.ADD
   
   point_marker.id=0
   point_marker.type=Type
   point_marker.scale.x=scale.x#0.1
   point_marker.scale.y=scale.y#0.1
   
   for i in data:
    point_marker.points.append(i)
   point_marker.colors.append(color[0])
   color[1].b = 1
   color[1].r = 0
   point_marker.colors.append(color[1])
   point_marker.lifetime=rospy.Duration(0.3)
   
   return point_marker
   
  if Type == Marker.ARROW:
   point_marker = Marker()
   point_marker.header.frame_id = '/map'
   point_marker.header.stamp = rospy.Time.now()
   point_marker.ns = 'plan_test'
   point_marker.action = Marker.ADD
   
   point_marker.id=0
   point_marker.type=Type
   point_marker.scale.x = scale.x * 5
   point_marker.scale.y = scale.y / 2
   point_marker.scale.z = scale.z / 2  
   point_marker.pose = data
   point_marker.pose.position.z = 2.5
   point_marker.color = copy.deepcopy(color)
   point_marker.color.g=2.0
   point_marker.lifetime=rospy.Duration(0.3)

   return point_marker


  if Type==Marker.LINE_LIST:
   #print 'pub LINE_LIST Marker'
   line_marker=Marker()
   line_marker.header.frame_id='/map'
   line_marker.header.stamp=rospy.Time.now()
   line_marker.ns='plan_test'
   line_marker.action=Marker.ADD
   
   line_marker.id=1
   line_marker.type=Type
   line_marker.scale.x=scale.x#0.05
   line_marker.scale.y=scale.y#0.05  
   
   line_marker.points=data
   for i in range(len(data)):
    line_marker.colors.append(color[i])

   line_marker.lifetime=rospy.Duration(0.5)
   
   return line_marker
 
 def PlotLines(self, path, num):
  Predict_Distance = num * 2
  Forward_Distance = num
  print '\n\ninto PlotLines'
  if len(self.path) >= (num + Predict_Distance):
   Front1 = copy.deepcopy(path[ : (num + Predict_Distance)])  
   Front2 = copy.deepcopy(path[ : (num + Forward_Distance)])
   color = ColorRGBA()
   color.a = 1
   color.r = 1
   colors = [color, color]
   color = ColorRGBA()
   color.b = 1
   color.a = 1
   colors.extend([color, color])
  
   points = [Front1[0].pose.position, Front1[-1].pose.position, Front2[0].pose.position, Front2[-1].pose.position]
  
  
   lines = self.visual_test(points, Marker.LINE_LIST, colors, self.scale)
  
   lines_pub = rospy.Publisher("/straight_lines", Marker ,queue_size=1)
   lines_pub.publish(lines)
   self.FrontMAX(Predict_Distance, Forward_Distance)
   

  print 'Predict_Distance: ', Predict_Distance, 'Forward_Distance: ', Forward_Distance
  #print 'PlotLines:'
  #print Front1[0].pose.position
  #print Front1[-1].pose.position
  #print Front2[0].pose.position
  #print Front2[-1].pose.position
  #print 'PlotLines_end '

   
 def FrontMAX(self, Predict_Distance, Forward_Distance):

  FrontLine = CVlib.SLF()
  
  Front1 = copy.deepcopy(self.path[: Predict_Distance])
  (Line1, CoefficientA1, CoefficientB1, CoefficientC1) = FrontLine.OLS(Front1) 
  
  Front2 = copy.deepcopy(self.path[: Forward_Distance])
  (Line2, CoefficientA2, CoefficientB2, CoefficientC2) = FrontLine.OLS(Front2)  
   
  Coe1 = [CoefficientA1, CoefficientB1]
  Coe2 = [CoefficientA2, CoefficientB2]
  
  #SimilarLines = FrontLine.get_similar_lines(Coe1, Coe2)
  SimilarLines = FrontLine.Orientation_line_com(self.odom.orientation, Coe1)
  
  print 'Line1: ', (Line1, CoefficientA1, CoefficientB1, CoefficientC1)
  print 'Line2: ', (Line1, CoefficientA2, CoefficientB2, CoefficientC2)
  
  #print 'Line1 ratio: ', -CoefficientA1/CoefficientB1, ' Line2 ratio: ', -CoefficientA2/CoefficientB2
  #print 'odom angle: ',  self.a_odom, ' tan: ', numpy.tan(self.a_odom), ' sin: ', numpy.sin(self.a_odom), ' cos: ', numpy.cos(self.a_odom)
  
  if SimilarLines:
   print 'paral: ',  True
  else:
   print 'paral: ',  False
   pass

if __name__=='__main__':
 rospy.init_node('Plantest')
 try:
  rospy.loginfo( "initialization system")
  Plantest()
  print "process done and quit"
 except rospy.ROSInterruptException:
  rospy.loginfo("node terminated.")


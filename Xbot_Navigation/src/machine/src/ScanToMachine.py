#!/usr/bin/env python
"""
Copyright (c) Xu Zhihao (Howe).  All rights reserved.

This program is free software; 

you can redistribute it and/or modify This programm is tested on kuboki base 

turtlebot. 

"""
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Pose
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point

class ScanToMachine():
 def __init__(self):
  self.define()
  rospy.Subscriber('/scan', LaserScan, self.laser_cb)
  rospy.Subscriber('/odom',Odometry,self.pose_cb)
  rospy.spin()
  
 def define(self):
  self.distance = None
  self.odom = Pose()
  self.robot = Marker()
  self.robot.header.frame_id = 'map'
  self.robot_pub = rospy.Publisher("/robot_position", Marker ,queue_size=1)
  self.color = ColorRGBA()
  self.scale = Point()
  self.scale.x=0.05
  self.scale.y=0.05
  self.color.r=2.0
  self.color.g=0.0
  self.color.b=0.0
  self.color.a=1.0
  self.laser = []

 def laser_cb(self, data):
  j = 0.0
  for i in data.ranges:
   if i > 0.0:
    self.laser.append(i)
  self.distance = min(self.laser)
  print 'distance is: ', self.distance
  
 def pose_cb(self, data):
  odom = data.pose.pose
  odom.position.z = 0.5
  self.robot = self.visual_test(odom.position, Marker.POINTS, self.color, self.scale)
  self.robot_pub.publish(self.robot)
  
 def visual_test(self,data,Type,color,scale):
  point_marker=Marker()
  point_marker.header.frame_id='/map'
  point_marker.header.stamp=rospy.Time.now()
  point_marker.ns='robot_test'
  point_marker.action=Marker.ADD
   
  point_marker.id=0
  point_marker.type=Type
  point_marker.scale.x=scale.x#0.1
  point_marker.scale.y=scale.y#0.1
   
  point_marker.points = [data]
  point_marker.colors = [color]

  point_marker.lifetime=rospy.Duration(0.3)
   
  return point_marker
   
if __name__=='__main__':
 try:
  rospy.init_node('ScanToMachine')
  rospy.loginfo ("initialization system")
  ScanToMachine()
  rospy.loginfo ("process done and quit")
  rospy.loginfo('path getted')
 except rospy.ROSInterruptException:
  rospy.loginfo("robot twist node terminated.")

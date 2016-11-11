#!/usr/bin/env python
"""
Copyright (c) Xu Zhihao (Howe).  All rights reserved.

This program is free software; 

you can redistribute it and/or modify This programm is tested on kuboki base 

turtlebot. 

"""
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class MoveCircle():
 def __init__(self):
  self.define()
  rospy.Subscriber('/scan', LaserScan, self.laser_cb)
  rospy.spin()
  
 def define(self):
  self.topice = '/navigation_velocity_smoother/raw_cmd_vel'
  #self.topice = '/cmd_vel_mux/input/teleop'
  self.cmd_vel = rospy.Publisher(self.topice , Twist, queue_size=5)
  self.cmd = Twist()
  self.distance = None
  self.laser = []
  
 def laser_cb(self, data):
  j = 0.0
  for i in data.ranges:
   if i > 0.0:
    self.laser.append(i)
  self.distance = min(self.laser)
  if self.distance < 0.5:
   self.cmd = Twist()
   #self.cmd_vel.publish(self.cmd)
  else:
   self.cmd.linear.x = 0.1
   self.cmd.angular.z = 0.2
   self.cmd_vel.publish(self.cmd)


if __name__=='__main__':
 try:
  rospy.init_node('MoveCircle')
  rospy.loginfo ("initialization system")
  MoveCircle()
  rospy.loginfo ("process done and quit")
  rospy.loginfo('path getted')
 except rospy.ROSInterruptException:
  rospy.loginfo("robot twist node terminated.")

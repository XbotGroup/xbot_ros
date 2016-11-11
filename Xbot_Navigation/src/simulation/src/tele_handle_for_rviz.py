#!/usr/bin/env python
""" tele handle.py 

- Version 1.0 2015/8/31

this file is used to transfer teleop to simulator

Copyright (c) 2015 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot. 

"""
""" 
priority:
  - name:        "Default input"
    topic:       "cmd_vel"
    priority:    0
    short_desc:  "Default velocity topic; controllers unaware that we are multiplexing cmd_vel will come here"
    
  - name:        "Navigation stack"
    topic:       "nav_cmd_vel"
    priority:    1
    short_desc:  "ROS navigation stack controller"
    
  - name:        "Onboard joystick"
    topic:       "joy_cmd_vel"
    priority:    10
    
  - name:        "Remote control"
    topic:       "rem_cmd_vel"
    priority:    9
    
  - name:        "Web application"
    topic:       "web_cmd_vel"
    priority:    8
    
  - name:        "Keyboard operation"
    topic:       "key_cmd_vel"
    priority:    7
    
"""

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
import copy

class TeleHandle():
 def define(self):
  self.priority = 0
  self.CMD = {0: Twist(), 1:None, 2:None}
  self.block_navi = False

 def TeleopCB(self, data):
  print 'TeleopCB'
  TeleopData=Twist()
  TeleopData.linear.x=data.linear.x
  TeleopData.linear.y=data.linear.y
  TeleopData.linear.z=data.linear.z

  TeleopData.angular.x=data.angular.x
  TeleopData.angular.y=data.angular.y
  TeleopData.angular.z=data.angular.z
  
  self.priority = 1
  self.CMD[1] = TeleopData
  self.block_navi = True
  
  
 def NaviCB(self, data):
  print 'NaviCB'
  NaviData=Twist()
  NaviData.linear.x=data.linear.x
  NaviData.linear.y=data.linear.y
  NaviData.linear.z=data.linear.z

  NaviData.angular.x=data.angular.x
  NaviData.angular.y=data.angular.y
  NaviData.angular.z=data.angular.z
  
  if not  self.block_navi:
   self.priority = 2
  self.CMD[2] = NaviData

 
 def PubCMD(self, priority):
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  cmd = self.CMD[copy.deepcopy(self.priority)]
  #rospy.loginfo(cmd)
  pub.publish(cmd)
  self.priority = 0
  #print cmd
  #cmd = Twist()
 
 def PriorityHandle(self, event):
  self.block_navi = False
 
 
 def __init__(self):
  rospy.init_node('tele_handle', anonymous=True)
  self.define()
  rospy.Subscriber('/cmd_vel_mux/input/teleop',Twist, self.TeleopCB)
  rospy.Subscriber('/cmd_vel_mux/input/navi',Twist, self.NaviCB)
  rospy.Timer(rospy.Duration(0.5), self.PubCMD)
  rospy.Timer(rospy.Duration(1), self.PriorityHandle)
  rospy.spin()

if __name__ == '__main__':
 TeleHandle()

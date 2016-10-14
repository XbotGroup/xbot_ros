#!/usr/bin/env python
#coding=utf-8
""" 
this code is used for making one marker in map

Copyright (c) 2016 rocwang.  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot. 

"""

import rospy,std_msgs.msg
from geometry_msgs.msg import PointStamped,Point
from visualization_msgs.msg import Marker
from nav_msgs.msg import Odometry


class dynamic_add_obstacles():
 def define(self):
  self.marker=Marker()
  # self.marker.color.r=1.0
  # self.marker.color.g=0.0
  # self.marker.color.b=0.0
  # self.marker.color.a=1.0
  self.marker.id = 0
  self.marker.ns='dynamic_3d_view'
  self.marker.scale.x=1
  self.marker.scale.y=1
  self.marker.scale.z=1
  self.marker.header.stamp =rospy.Time.now()
  self.marker.header.frame_id='map'

  self.marker.type=10
  self.marker.mesh_resource="package://dynamic_3d_view/dynamic_model/plant1/plant1.DAE"
  self.marker.mesh_use_embedded_materials=1
  self.marker.action=0

  self.marker.lifetime = rospy.Duration(0)  
  self.marker_pub=rospy.Publisher("dynamic_add_obstacles",Marker,queue_size=1)
  self.count=0
  self.period=rospy.Duration(0.3)
  self.trigger=False
  self.trigger_pub = rospy.Publisher('empty_marker', std_msgs.msg.Bool, queue_size=1)

 def sub_callback(self,pose):
  self.count=self.count+1
  if not rospy.has_param('~goal_number'):
   rospy.set_param('~goal_number',3)
  else:
   pass
  goal_number=rospy.get_param('~goal_number')
  if self.count>=goal_number:
   self.trigger_pub.publish(True)
  self.update_odom()

  # self.marker.points.append(pose.point)
  #print len(self.marker.points)
  self.marker.pose.position=pose.point
  print self.marker.pose
  self.marker_pub.publish(self.marker)
  
 def timer(self,event):
  if self.clear:
   self.clear=False
   self.define()
   
 def update_odom(self):
  self.marker.points=[]

   
 def empty_callback(self,trigger):
  if trigger.data:
   self.clear=True
   rospy.Timer(self.period, self.timer)
  else:
   pass
   
   
 def __init__(self):
  self.clear=True 
  rospy.init_node('dynamic_add_obstacles')
  rospy.loginfo ('请使用publish point选出想要添加障碍物的地方')
  self.define()
  rospy.Timer(self.period, self.timer)
  rospy.Subscriber('empty_marker', std_msgs.msg.Bool, self.empty_callback)
  rospy.Subscriber("clicked_point",PointStamped,      self.sub_callback)
  rospy.spin()


if __name__=='__main__':
 try:
  rospy.loginfo ("initialization system")
  dynamic_add_obstacles()
  rospy.loginfo ("process done and quit")
 except rospy.ROSInterruptException:
  rospy.loginfo("robot twist node terminated.")

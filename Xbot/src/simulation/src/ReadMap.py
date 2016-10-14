#!/usr/bin/env python
#coding=utf-8
"""
rviz 地图编辑软件测试算法用

This programm is tested on kuboki base turtlebot. 
Copyright (c) Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
import numpy
import rospy
import yaml
from nav_msgs.msg import OccupancyGrid 
import Image
import copy
from geometry_msgs.msg import Pose
from threading import Lock
import maplib
from geometry_msgs.msg import PoseArray
from std_msgs.msg import String
from nav_msgs.msg import MapMetaData 
from nav_msgs.srv import *


class grid_map():
 def __init__(self):
  self.define()
  self.init_map = self.ReadPGMMap()
  self.Map =  copy.deepcopy(self.init_map)
  self.start = True
  self.segments = 50
  """#try:
   #rospy.Subscriber(self.root_topic+'/projection', PointStamped, self.MessPosition, queue_size=1)
   #rospy.Subscriber(self.root_topic+'/projection'+'/size', String, self.Size, queue_size=1)
  #except:"""
  rospy.Subscriber(self.root_topic+'/projection', PoseArray , self.MessPoses, queue_size=1)
  rospy.Timer(rospy.Duration(15), self.Reload)
  rospy.Timer(rospy.Duration(0.5), self.Clear)
  self.AMCLMapSever()
  rospy.spin()
  
 """def Size(self, data):
  #print 'data', data
  with self.locker:
   self.radiu = data.data
  #print 'Size', self.radiu"""
 
 def AMCLMapSever(self):
  with self.locker: 
   MapServer = rospy.Service('/static_map', GetMap, self.mapCallback)
  
 def mapCallback(self, req):
  with self.locker: 
   rospy.loginfo('sending map')
   res = self.Map
   return res

 def MessPoses(self, poses):
  with self.locker: 
   if len(poses.poses) > 0:
    self.Map.data = copy.deepcopy(self.init_map.data)
    #print 'MessPoses'
    for pose in poses.poses:
     num = maplib.position_num(self.Map, pose.position)
     self.Map.data[num] = 100
   self.map_pub.publish(self.Map)
   
 """def MessPosition(self, position):
  with self.locker: 
   num = maplib.position_num(self.Map, position.point)
   #print num,len(self.Map.data)#,cmp(self.Map.data, self.init_map.data)
   self.Map.data = copy.deepcopy(self.init_map.data)
   #print self.radiu
   if self.radiu != 'None':
    self.Map.data[num] = 100 
    size = int((float(self.radiu)))
    unit = numpy.pi / self.segments     

   else:
    print 'default'
    size = 1
    size = int(size*10/2)
    for i in range(size):
     #self.Map.data[num+i] = 100
     #self.Map.data[num+i*self.Map.info.width] = 100
     for j in range(size):
      self.Map.data[num+i*self.Map.info.width + j] = 100
      self.Map.data[num+i*self.Map.info.width - j] = 100
     
    for i in range(size):
     #self.Map.data[num-i] = 100
     #self.Map.data[num-i*self.Map.info.width] = 100
     for j in range(size):
      self.Map.data[num-i*self.Map.info.width + j] = 100
      self.Map.data[num-i*self.Map.info.width - j] = 100

   #print 'MessPosition'
   self.map_pub.publish(self.Map)"""

 def Reload(self, event):
  with self.locker:
   self.Map.data = copy.deepcopy(self.init_map.data)
   self.map_pub.publish(self.Map)
   #print 'repub' 
   self.PubMetadata()
   
 def Clear(self,event):
  with self.locker:
   if self.start:
    self.map_pub.publish(self.init_map)
    self.start = False
    #print 'clear'
   else:
    self.map_pub.publish(self.Map)
   self.PubMetadata()
   #print maplib.get_effective_point(self.Map)[1]
  
  
 def PubMetadata(self): 
  self.map_metadata.publish(self.Map.info)
  
 def define(self):
  self.locker = Lock()

  if not rospy.has_param('~map_file'):
   rospy.set_param('~map_file','/home/howe/cafe_robot_single/src/nav_staff/map/')
  else:
   self.filename = rospy.get_param('~map_file')

  self.map_pub=rospy.Publisher("/map", OccupancyGrid ,queue_size=1)
  self.map_metadata=rospy.Publisher("/map_metadata", MapMetaData ,queue_size=1)
  self.root_topic='/test_obstacles'
  #self.radiu = numpy.inf
  
  if not rospy.has_param('~frame_id'):
   rospy.set_param('~frame_id','/map')
  self.frame_id = rospy.get_param('~frame_id')

  if not rospy.has_param('~use_map_topic'):
   rospy.set_param('~use_map_topic','/map')

  
 def ReadPGMMap(self):
  (self.image,self.resolution,self.origin,self.load_time) = self.ReadYaml()
   
  f=Image.open(self.filename+self.image)
  (width,height)=f.size
  GridMap=numpy.array(f)
  
  Map=OccupancyGrid()
  Map.header.frame_id=self.frame_id
  Map.info.width=width
  Map.info.height=height
  Map.info.resolution=self.resolution
  Map.info.origin.position.x=self.origin[0]
  Map.info.origin.position.y=self.origin[1]
  Map.info.origin.position.z=self.origin[2]
  Map.info.origin.orientation.w=1
  #print 'height',height,'width',width
  for i in range(height):
   data=GridMap[height-i-1]
   for j in data:
    res=j==[0,0,0]
    if res.all():
     Map.data.append(100)
    else:
     Map.data.append(0)
  #print Map.info
  return Map
   
 def ReadYaml(self):
  with open(self.filename+'office_map_manual.yaml', 'rb') as f:
   data = yaml.load(f)
  image = data['image']
  resolution = data['resolution']
  origin = data['origin']
  load_time = rospy.Time.now()
  return (image,resolution,origin,load_time)
  
   
if __name__=='__main__':
 rospy.init_node('grid_map')
 try:
  rospy.loginfo ("initialization system")
  grid_map()
  rospy.loginfo ("process done and quit")
 except rospy.ROSInterruptException:
  rospy.loginfo("robot twist node terminated.")

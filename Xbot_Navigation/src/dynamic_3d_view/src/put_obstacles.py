#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-
# @Author: rocwang
# @Date:   2016-05-30 17:15:11
# @Last Modified by:   rocwang
# @Last Modified time: 2016-06-06 15:23:43

import rospy,std_msgs.msg
from geometry_msgs.msg import PointStamped,Point
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray



topic = 'put_obstacles'
publisher = rospy.Publisher(topic, MarkerArray,queue_size=1)

rospy.init_node('put_obstacles')

markerArray = MarkerArray()


f=open('package://dynamic_3d_view/config/obstacles.txt','rb')
data=f.read().split('\n')
f.close()
num_obs=(len(data)-1)/3
switch={1:"plant/plant.DAE",2:"plant1/plant1.DAE",3:"dog/dog.DAE",4:"bianji2/bianji2.DAE"}
for x in xrange(0,num_obs):
		kind=int(data[3*x])
		px=float(data[3*x+1])
		py=float(data[3*x+2])
		filename="package://dynamic_3d_view/dynamic_model/"+switch[kind]
		# print filename
		marker = Marker()
		marker.id = x
		marker.header.frame_id = "/map"
		marker.ns='put_obstacles'
		marker.type=10
		marker.scale.x=1
		marker.scale.y=1
		marker.scale.z=1
		# marker.header.stamp =rospy.Time.now()
		marker.mesh_resource=filename
		marker.mesh_use_embedded_materials=1
		marker.action=0
		# marker.lifetime = rospy.Duration(0) 
		marker.pose.position.x = px-6.5
		marker.pose.position.y = py-6.5
		marker.pose.position.z = 0
		markerArray.markers.append(marker)
		
while not rospy.is_shutdown():
	# Publish the MarkerArray
	publisher.publish(markerArray)
	rospy.sleep(1)
	


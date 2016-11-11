# Real machine 
1. roslaunch machine xbot_bringup.launch
2. roslaunch machine Xbot_amcl.launch
3. roslaunch machine 3D_RVIZ.launch
4. rosrun nav_staff init_pose_handle.py
5. rosrun nav_staff keyboard_control.py
6. roslaunch machine robot_controller_cruise.launch
OR
6. roslaunch machine robot_controller_single.launch


# robot_controller_
1. roslaunch amcl_odom turtlebot_position_in_map.launch
2. roslaunch marker robot_uni_marker.launch
3. roslaunch marker ui_marker.launch
4. rosrun obstacle_warning DetectorStopMove.py 
5. roslaunch camera_image camera_image.launch 
6. roslaunch simple_voice warning_speaker.launch
7. rosrun tasks go_tasks.py


# new move_base
1. roslaunch simulation fake_robot.launch
2. roslaunch simulation fake_amcl.launch
3. roslaunch machine robot_controller_single.launch
4. roslaunch machine 3D_RVIZ.launch
5. rosrun nav_staff keyboard_control.py
6. rosrun simulation tele_handle_for_rviz.py
7. rosrun nav_staff base_controller.py
测试：
8. rosrun nav_staff Plantest.py #testing plan

# new move_base
1. roslaunch machine xbot_bringup.launch
2. roslaunch machine Xbot_amcl.launch
3. roslaunch machine 3D_RVIZ.launch
4. rosrun nav_staff init_pose_handle.py
5. rosrun nav_staff keyboard_control.py
6. roslaunch machine robot_controller_single.launch


# 仿真步骤
1. roslaunch simulation fake_robot.launch

2. roslaunch simulation fake_amcl.launch
OR 
2. 
roslaunch simulation fake_amcl_withoutmap.launch
rosrun simulation ReadMap.py

3. roslaunch machine 3D_RVIZ.launch

4. roslaunch machine robot_controller_single.launch

5. rosrun nav_staff init_pose_handle.py

6. rosrun nav_staff keyboard_control.py

7. rosrun simulation tele_handle_for_rviz.py

8. rosrun simulation interactive_marker.py

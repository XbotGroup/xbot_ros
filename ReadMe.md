all you need is launch xbot bringup and then flow flowing steps:
1. roslaunch machine Xbot_amcl.launch (launch the amcl for xbot)
2. roslaunch machine 3D_RVIZ.launch (launch 3D_RVIZ for xbot)
3. rosrun nav_staff init_pose_handle.py (initialise init position for xbot)

4. rosrun nav_staff keyboard_control.py (use keyboard to controal robot)

OR, you can use multi task module, to let robot navigate between serveral points , in this module the only thing you need is to figure out goals number and goals in map.

4. roslaunch machine robot_controller_cruise.launch


# new move_base
0. roslaunch machine xbot_bringup.launch
1. roslaunch machine Xbot_amcl.launch (launch the amcl for xbot)
2. roslaunch machine robot_controller_single.launch (single task module)
3. roslaunch machine 3D_RVIZ.launch (launch 3D_RVIZ for xbot)
4. rosrun nav_staff keyboard_control.py (use keyboard to controal robot)
5. rosrun nav_staff init_pose_handle.py (initialise init position for xbot)
OR
5. roslaunch machine robot_controller_cruise.launch

# new move_base simulation
# the differences between fake simulation and real running are amcl localization and control base.
# in simulation, amcl use fake localizetion replaced
# control base in simulation only has two command priority, one is cmd_vel_mux/input/teleop the other is /cmd_vel_mux/input/navi
 
1. roslaunch simulation fake_robot.launch
2. roslaunch simulation fake_amcl.launch
3. roslaunch machine robot_controller_single.launch
4. roslaunch machine 3D_RVIZ.launch
5. rosrun nav_staff keyboard_control.py
6. rosrun simulation tele_handle_for_rviz.py
7. rosrun nav_staff base_controller.py
测试：
8. rosrun nav_staff Plantest.py

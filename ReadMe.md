all you need is launch xbot bringup and then flow flowing steps:
1. roslaunch machine Xbot_amcl.launch (launch the amcl for xbot)
2. roslaunch machine 3D_RVIZ.launch (launch 3D_RVIZ for xbot)
3. rosrun nav_staff init_pose_handle.py (initialise init position for xbot)

4. rosrun nav_staff keyboard_control.py (use keyboard to controal robot)

OR, you can use multi task module, to let robot navigate between serveral points , in this module the only thing you need is to figure out goals number and goals in map.

4. roslaunch machine robot_controller_cruise.launch


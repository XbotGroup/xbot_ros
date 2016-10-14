# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "xbot_msgs: 18 messages, 0 services")

set(MSG_I_FLAGS "-Ixbot_msgs:/home/howe/Xbot/src/xbot/xbot_msgs/msg;-Ixbot_msgs:/home/howe/Xbot/devel/share/xbot_msgs/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/indigo/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(xbot_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg" "xbot_msgs/AutoDockingGoal:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg" "xbot_msgs/AutoDockingFeedback:actionlib_msgs/GoalStatus:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg" "xbot_msgs/AutoDockingResult:xbot_msgs/AutoDockingActionResult:actionlib_msgs/GoalStatus:actionlib_msgs/GoalID:xbot_msgs/AutoDockingGoal:xbot_msgs/AutoDockingActionGoal:std_msgs/Header:xbot_msgs/AutoDockingFeedback:xbot_msgs/AutoDockingActionFeedback"
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg" NAME_WE)
add_custom_target(_xbot_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_msgs" "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg" "xbot_msgs/AutoDockingResult:actionlib_msgs/GoalStatus:actionlib_msgs/GoalID:std_msgs/Header"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_cpp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(xbot_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(xbot_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(xbot_msgs_generate_messages xbot_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_cpp _xbot_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_msgs_gencpp)
add_dependencies(xbot_msgs_gencpp xbot_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_msgs_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)
_generate_msg_lisp(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(xbot_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(xbot_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(xbot_msgs_generate_messages xbot_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_lisp _xbot_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_msgs_genlisp)
add_dependencies(xbot_msgs_genlisp xbot_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_msgs_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)
_generate_msg_py(xbot_msgs
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/indigo/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(xbot_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(xbot_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(xbot_msgs_generate_messages xbot_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/MotorPower.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/RobotStateEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/KeyboardInput.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ControllerInfo.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/PowerSystemEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/DockInfraRed.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/WheelDropEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/ScanAngle.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/CliffEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/SensorState.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingFeedback.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_msgs/msg/BumperEvent.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingAction.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingGoal.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/devel/share/xbot_msgs/msg/AutoDockingActionResult.msg" NAME_WE)
add_dependencies(xbot_msgs_generate_messages_py _xbot_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_msgs_genpy)
add_dependencies(xbot_msgs_genpy xbot_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(xbot_msgs_generate_messages_cpp actionlib_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(xbot_msgs_generate_messages_lisp actionlib_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_msgs_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(xbot_msgs_generate_messages_py actionlib_msgs_generate_messages_py)

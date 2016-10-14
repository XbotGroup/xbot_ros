# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "xbot_bringup: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ixbot_bringup:/home/howe/Xbot/src/xbot/xbot_bringup/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Ivisualization_msgs:/opt/ros/indigo/share/visualization_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(xbot_bringup_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg" NAME_WE)
add_custom_target(_xbot_bringup_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_bringup" "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg" ""
)

get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg" NAME_WE)
add_custom_target(_xbot_bringup_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xbot_bringup" "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_bringup
)
_generate_msg_cpp(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_bringup
)

### Generating Services

### Generating Module File
_generate_module_cpp(xbot_bringup
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_bringup
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(xbot_bringup_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(xbot_bringup_generate_messages xbot_bringup_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_cpp _xbot_bringup_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_cpp _xbot_bringup_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_bringup_gencpp)
add_dependencies(xbot_bringup_gencpp xbot_bringup_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_bringup_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_bringup
)
_generate_msg_lisp(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_bringup
)

### Generating Services

### Generating Module File
_generate_module_lisp(xbot_bringup
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_bringup
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(xbot_bringup_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(xbot_bringup_generate_messages xbot_bringup_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_lisp _xbot_bringup_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_lisp _xbot_bringup_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_bringup_genlisp)
add_dependencies(xbot_bringup_genlisp xbot_bringup_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_bringup_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup
)
_generate_msg_py(xbot_bringup
  "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup
)

### Generating Services

### Generating Module File
_generate_module_py(xbot_bringup
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(xbot_bringup_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(xbot_bringup_generate_messages xbot_bringup_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_state.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_py _xbot_bringup_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/howe/Xbot/src/xbot/xbot_bringup/msg/xbot_cmd.msg" NAME_WE)
add_dependencies(xbot_bringup_generate_messages_py _xbot_bringup_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xbot_bringup_genpy)
add_dependencies(xbot_bringup_genpy xbot_bringup_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xbot_bringup_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_bringup)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xbot_bringup
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_bringup_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(xbot_bringup_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(xbot_bringup_generate_messages_cpp visualization_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_bringup)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xbot_bringup
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_bringup_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(xbot_bringup_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(xbot_bringup_generate_messages_lisp visualization_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xbot_bringup
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(xbot_bringup_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(xbot_bringup_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(xbot_bringup_generate_messages_py visualization_msgs_generate_messages_py)

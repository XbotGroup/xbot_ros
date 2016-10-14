; Auto-generated. Do not edit!


(cl:in-package xbot_bringup-msg)


;//! \htmlinclude xbot_state.msg.html

(cl:defclass <xbot_state> (roslisp-msg-protocol:ros-message)
  ((power
    :reader power
    :initarg :power
    :type cl:float
    :initform 0.0))
)

(cl:defclass xbot_state (<xbot_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <xbot_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'xbot_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xbot_bringup-msg:<xbot_state> is deprecated: use xbot_bringup-msg:xbot_state instead.")))

(cl:ensure-generic-function 'power-val :lambda-list '(m))
(cl:defmethod power-val ((m <xbot_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xbot_bringup-msg:power-val is deprecated.  Use xbot_bringup-msg:power instead.")
  (power m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <xbot_state>) ostream)
  "Serializes a message object of type '<xbot_state>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'power))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <xbot_state>) istream)
  "Deserializes a message object of type '<xbot_state>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'power) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<xbot_state>)))
  "Returns string type for a message object of type '<xbot_state>"
  "xbot_bringup/xbot_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xbot_state)))
  "Returns string type for a message object of type 'xbot_state"
  "xbot_bringup/xbot_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<xbot_state>)))
  "Returns md5sum for a message object of type '<xbot_state>"
  "b75f3bcdec2dcafb6503e9b6316400b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'xbot_state)))
  "Returns md5sum for a message object of type 'xbot_state"
  "b75f3bcdec2dcafb6503e9b6316400b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<xbot_state>)))
  "Returns full string definition for message of type '<xbot_state>"
  (cl:format cl:nil "float32 power~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'xbot_state)))
  "Returns full string definition for message of type 'xbot_state"
  (cl:format cl:nil "float32 power~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <xbot_state>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <xbot_state>))
  "Converts a ROS message object to a list"
  (cl:list 'xbot_state
    (cl:cons ':power (power msg))
))

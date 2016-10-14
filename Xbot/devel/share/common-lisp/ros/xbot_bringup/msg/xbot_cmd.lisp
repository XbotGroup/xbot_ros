; Auto-generated. Do not edit!


(cl:in-package xbot_bringup-msg)


;//! \htmlinclude xbot_cmd.msg.html

(cl:defclass <xbot_cmd> (roslisp-msg-protocol:ros-message)
  ((cmd
    :reader cmd
    :initarg :cmd
    :type cl:string
    :initform "")
   (args
    :reader args
    :initarg :args
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass xbot_cmd (<xbot_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <xbot_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'xbot_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name xbot_bringup-msg:<xbot_cmd> is deprecated: use xbot_bringup-msg:xbot_cmd instead.")))

(cl:ensure-generic-function 'cmd-val :lambda-list '(m))
(cl:defmethod cmd-val ((m <xbot_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xbot_bringup-msg:cmd-val is deprecated.  Use xbot_bringup-msg:cmd instead.")
  (cmd m))

(cl:ensure-generic-function 'args-val :lambda-list '(m))
(cl:defmethod args-val ((m <xbot_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader xbot_bringup-msg:args-val is deprecated.  Use xbot_bringup-msg:args instead.")
  (args m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <xbot_cmd>) ostream)
  "Serializes a message object of type '<xbot_cmd>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'cmd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'cmd))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'args))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'args))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <xbot_cmd>) istream)
  "Deserializes a message object of type '<xbot_cmd>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cmd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'cmd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'args) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'args)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<xbot_cmd>)))
  "Returns string type for a message object of type '<xbot_cmd>"
  "xbot_bringup/xbot_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xbot_cmd)))
  "Returns string type for a message object of type 'xbot_cmd"
  "xbot_bringup/xbot_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<xbot_cmd>)))
  "Returns md5sum for a message object of type '<xbot_cmd>"
  "6723d032225dfb791e3b4b487d839111")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'xbot_cmd)))
  "Returns md5sum for a message object of type 'xbot_cmd"
  "6723d032225dfb791e3b4b487d839111")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<xbot_cmd>)))
  "Returns full string definition for message of type '<xbot_cmd>"
  (cl:format cl:nil "string cmd~%float32[] args~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'xbot_cmd)))
  "Returns full string definition for message of type 'xbot_cmd"
  (cl:format cl:nil "string cmd~%float32[] args~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <xbot_cmd>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'cmd))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'args) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <xbot_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'xbot_cmd
    (cl:cons ':cmd (cmd msg))
    (cl:cons ':args (args msg))
))

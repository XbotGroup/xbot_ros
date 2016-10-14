
(cl:in-package :asdf)

(defsystem "xbot_bringup-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "xbot_state" :depends-on ("_package_xbot_state"))
    (:file "_package_xbot_state" :depends-on ("_package"))
    (:file "xbot_cmd" :depends-on ("_package_xbot_cmd"))
    (:file "_package_xbot_cmd" :depends-on ("_package"))
  ))
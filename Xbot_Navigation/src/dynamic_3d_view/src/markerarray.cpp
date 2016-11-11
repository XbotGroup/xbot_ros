#include <ros/ros.h>
#include <visualization_msgs/Marker.h>
#include <visualization_msgs/MarkeArray.h>

int main( int argc, char** argv )
{
  ros::init(argc, argv, "init_gobal_3d_map");
  ros::NodeHandle n;
  ros::Rate r(1);
  ros::Publisher markerarray_pub = n.advertise<visualization_msgs::MarkerArray>("dynamic_bostacles", 1);  
  

  while (ros::ok())
  {
    visualization_msgs::MarkerArray markerarray;
    // Set the frame ID and timestamp.  See the TF tutorials for information on these.
    markerarray.header.frame_id = "/map";
    markerarray.header.stamp = ros::Time::now();

    // Set the namespace and id for this markerarray.  This serves to create a unique ID
    // Any markerarray sent with the same namespace and id will overwrite the old one
    markerarray.ns = "init_global_3d_map";
    markerarray.id = 0;

    // Set the markerarrayarray type.  Initially this is CUBE, and cycles between that and SPHERE, ARROW, and CYLINDER
    markerarray.type = visualization_msgs::MarkerArray::MESH_RESOURCE;
    markerarray.mesh_resource = "package://dynamic_3d_view/map_3d/5-9-L2/office.DAE";

    // Set the markerarray action.  Options are ADD, DELETE, and new in ROS Indigo: 3 (DELETEALL)
    markerarray.action = visualization_msgs::markerarray::ADD;

    // Set the pose of the markerarray.  This is a full 6DOF pose relative to the frame/time specified in the header
    markerarray.pose.position.x = -6.91;
    markerarray.pose.position.y = -0.90;
    markerarray.pose.position.z = -0.2;
    markerarray.pose.orientation.x = 0.0;
    markerarray.pose.orientation.y = 0.0;
    markerarray.pose.orientation.z = 0.0;
    markerarray.pose.orientation.w = 0.0;

    // Set the scale of the markerarray -- 1x1x1 here means 1m on a side
    markerarray.scale.x = 1.0;
    markerarray.scale.y = 1.0;
    markerarray.scale.z = 1.0;

    // Set the color -- be sure to set alpha to something non-zero!
    // markerarray.color.r = 0.7f;
    // markerarray.color.g = 0.7f;
    // markerarray.color.b = 0.7f;
    // markerarray.color.a = 1.0;
    markerarray.mesh_use_embedded_materials=1;

    markerarray.lifetime = ros::Duration();

    // Publish the markerarray
    while (markerarray_pub.getNumSubscribers() < 1)
    {
      if (!ros::ok())
      {
        return 0;
      }
      ROS_WARN_ONCE("Please create a subscriber to the markerarray");
      sleep(1);
    }
    markerarray_pub.publish(markerarray);

    

    r.sleep();
  }
}

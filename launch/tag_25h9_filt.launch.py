import launch
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
    
config = PathJoinSubstitution(
    [FindPackageShare("my_camera_bringup"), "config", "tags_25h9_filtered.yaml"]
)
print(config)

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/image_raw"), ("/apriltag/camera_info", "/camera_info")],
        parameters=[config])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])

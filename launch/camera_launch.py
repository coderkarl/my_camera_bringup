from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

cam_info_path = PathJoinSubstitution(
    [FindPackageShare("my_camera_bringup"), "config/camera_cal", "C615_640x320_ost.yaml"]
)
print(cam_info_path)

def generate_launch_description():
    return LaunchDescription([
        Node(
            name='opencv_cam',
            package='opencv_cam',
            executable='opencv_cam_main',
            output='screen',
            parameters=[{
                'index': 2,
                'fps': 10,  # A3
                'camera_frame_id': 'laser',
                'camera_info_path': cam_info_path,
                'width': 640,
                'height': 360,
            }],
            
            remappings=[('image_raw', 'camera/image_raw')]
        ),
    ])

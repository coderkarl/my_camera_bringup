# Camera Bringup  

## dependencies  
git clone https://github.com/clydemcqueen/opencv_cam.git  
git clone https://github.com/christianrauch/apriltag_msgs.git  
git clone https://github.com/christianrauch/apriltag_ros.git  

`sudo apt install ros-foxy-image-pipeline`  
`ros2 run camera_calibration cameracalibrator --size 7x9 --square 0.022 image:=/camera/image_raw camera:=/camera`  

`ros2 launch my_camera_bringup camera_launch.py`  
`ros2 launch my_camera_bringup tag_25h9_filt.launch.py`  

[https://github.com/AprilRobotics/apriltag/wiki/AprilTag-User-Guide](https://github.com/AprilRobotics/apriltag/wiki/AprilTag-User-Guide)

[https://roboticscasual.com/tutorial-ros2-launch-files-all-you-need-to-know/](https://roboticscasual.com/tutorial-ros2-launch-files-all-you-need-to-know/)

# saravia_pkg/launch/play_rviz_rqt.launch.py
import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    bag_path = os.path.join(
        os.getenv("HOME"),
        "ros2_ws/src/saravia_pkg/bag_files/nissan_zala_50_zeg_4_0.mcap"
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', bag_path],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
        ExecuteProcess(
            cmd=['rqt'],
            output='screen'
        )
    ])

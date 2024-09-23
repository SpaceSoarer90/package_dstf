from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    twist_stamper_node = Node(
            package='twist_stamper',
            executable='twist_stamper',
            remappings=[('/cmd_vel_in', '/diff_cont/cmd_vel_unstamped'), ('/cmd_vel_out', '/cmd_vel')]
         )

    return LaunchDescription([
        twist_stamper_node,
    ])
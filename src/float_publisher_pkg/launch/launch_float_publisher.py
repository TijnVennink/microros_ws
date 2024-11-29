import os
import sys
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='float_publisher_pkg',
            executable='float_publisher',
            name='float_publisher',
            output='screen',
            parameters=[],
            remappings=[]
        )
    ])
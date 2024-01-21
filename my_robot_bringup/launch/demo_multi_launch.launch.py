from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory



def generate_launch_description():
    ld = LaunchDescription()

    other_launch_description  = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('my_robot_bringup'),
                         'launch',
                         'test.launch.py'
            )
        )
    )

    ld.add_action(other_launch_description)

    return ld
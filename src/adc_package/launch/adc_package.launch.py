import os
from ament_index_python.packages import get_package_share_directory , get_search_paths
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import EnvironmentVariable
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    ros_namespace = LaunchConfiguration('ros_namespace')

    return LaunchDescription([
        DeclareLaunchArgument(
            'ros_namespace',
            default_value=os.environ['ROS_NAMESPACE'],
            description='Namespace of this module'
        ),
        Node(
            package='adc_package',
            node_executable='adc_talker',
            node_name='adc_talker',
            node_namespace=ros_namespace,
            output='screen'
        ),
    ])
    
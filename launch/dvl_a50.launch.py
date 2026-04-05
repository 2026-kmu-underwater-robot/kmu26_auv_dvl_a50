import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('ip_address', default_value='192.168.194.95'),
        launch.actions.DeclareLaunchArgument('velocity_frame_id', default_value='dvl'),
        launch.actions.DeclareLaunchArgument('position_frame_id', default_value='dvl'),
        launch_ros.actions.Node(
            package='dvl_a50',
            executable='dvl_a50_sensor',
            parameters=[{
                'dvl_ip_address': launch.substitutions.LaunchConfiguration('ip_address'),
                'velocity_frame_id': launch.substitutions.LaunchConfiguration('velocity_frame_id'),
                'position_frame_id': launch.substitutions.LaunchConfiguration('position_frame_id'),
            }],
            output='screen'),
    ])

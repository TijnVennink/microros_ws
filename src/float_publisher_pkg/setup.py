from setuptools import setup

package_name = 'float_publisher_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A simple ROS2 package to publish a float value to a topic.',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'float_publisher = float_publisher_pkg.float_publisher:main',
        ],
    },
)

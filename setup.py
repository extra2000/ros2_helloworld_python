from setuptools import setup

package_name = 'ros2_helloworld_python'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nick Aizuddin',
    maintainer_email='nick@extra2000.io',
    description='Simple helloworld example with Python',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld = ros2_helloworld_python.helloworld:main',
        ],
    },
)

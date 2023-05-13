import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class HelloWorld(Node):

    def __init__(self):
        super().__init__('helloworld')
        self.get_logger().info("Hello World! CTRL+C to exit!")

    def __del__(self):
        self.get_logger().info("Bye World!")


def main(args=None):
    rclpy.init(args=args)
    helloworld = HelloWorld()
    rclpy.spin(helloworld)
    helloworld.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

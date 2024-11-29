import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class FloatPublisher(Node):
    def __init__(self):
        super().__init__('float_publisher')
        self.publisher_ = self.create_publisher(Float32, 'motor_command', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0

    def timer_callback(self):
        msg = Float32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.data)
        self.i += 500.0

def main(args=None):
    rclpy.init(args=args)
    float_publisher = FloatPublisher()
    rclpy.spin(float_publisher)

if __name__ == '__main__':
    main()

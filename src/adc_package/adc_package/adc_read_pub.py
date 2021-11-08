import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Header
from cbm_interfaces.msg import AdcRaspi
import time
import RPi.GPIO as GPIO
from . import ADS1256

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('adc_read_pub')
        # TODO : message --> float array
        self.publisher_ = self.create_publisher(AdcRaspi, 'adc_8ch', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.ADC = ADS1256.ADS1256()
        if( self.ADC.ADS1256_init() == -1):
            print('adc initialization failure')

    def timer_callback(self):
        
        ADC_Value = self.ADC.ADS1256_GetAll()
        
        msg = AdcRaspi()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = (str(self.i))

        msg.ch0 = ADC_Value[0]*5.0/0x7fffff
        msg.ch1 = ADC_Value[1]*5.0/0x7fffff
        msg.ch2 = ADC_Value[2]*5.0/0x7fffff
        msg.ch3 = ADC_Value[3]*5.0/0x7fffff
        msg.ch4 = ADC_Value[4]*5.0/0x7fffff
        msg.ch5 = ADC_Value[5]*5.0/0x7fffff
        msg.ch6 = ADC_Value[6]*5.0/0x7fffff
        msg.ch7 = ADC_Value[7]*5.0/0x7fffff
        
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%f"' % msg.ch0)
        #self.get_logger().info('Publishing: "%f"' % self.get_clock().now().to_msg().sec)
        self.i += 1
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
import numpy
import serial
import struct
from rclpy.node import Node

from geometry_msgs.msg import TwistStamped

class MecanumDrive(Node):

    def __init__(self):
        super().__init__('mecanum_drive')
        self.subscription = self.create_subscription(
            TwistStamped,
            'cmd_vel',
            self.mecanum_drive_callback,
            10)
        self.subscription
        self.serial = serial.Serial('/dev/ttyUSB0', 115200)

    
    def mecanum_drive_callback(self, msg):
        l_x = numpy.float32(msg.twist.linear.x)
        l_y = numpy.float32(msg.twist.linear.y)
        r_z = numpy.float32(msg.twist.angular.z)

        print(float_to_bin(l_x) + '|' + float_to_bin(r_z))

        self.serial.write(float_to_bin(l_x).encode('ascii') + b'|')
        self.serial.write(float_to_bin(r_z).encode('ascii') + b'\n')


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def main(args=None):
    rclpy.init(args=args)

    mecanum_drive = MecanumDrive()

    rclpy.spin(mecanum_drive)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


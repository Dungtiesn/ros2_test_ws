#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("MyNode")
        self.get_logger().info("Starting MyNode")
        self.create_timer(0.5, self.timer_callback)
        self.counter_  = 0 

    def timer_callback(self):
        self.get_logger().info("Callback " + str(self.counter_))
        self.counter_ = self.counter_ + 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class TurtlerController(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.previous_x = 0
        self.get_logger().info(" Turtle Controller Start")
        self.cmd_vel_pub = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self.pose_subcriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, pose:Pose):
        cmd = Twist()
        
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 0.5
            cmd.angular.z = 1.0
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        
        if pose.x > 5.5 and self.previous_x <= 5.5:
            self.previous_x = pose.x
            self.get_logger().info("Red")
            self.call_set_pen_service(255, 0, 0, 3, 0)
        elif pose.x <= 5.5 and self.previous_x > 5.5:
            self.previous_x = pose.x
            self.get_logger().info("Green")
            self.call_set_pen_service(0, 255, 0, 3, 0)

        self.cmd_vel_pub.publish(cmd)

    def call_set_pen_service(self, r, b, g, width, off):
        client  = self.create_client(
            SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service")

        request = SetPen.Request()
        request.r = r
        request.b = b
        request.g = g
        request.width = width 
        request.off = off

        future_obj = client.call_async(request)
        future_obj.add_done_callback(partial(self.callback_set_pen))
    def callback_set_pen(self, future_obj):
        try:
            response = future_obj.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %s" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = TurtlerController()
    rclpy.spin(node)
    rclpy.shutdown()
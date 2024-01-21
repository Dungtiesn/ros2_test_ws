#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisherNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, '/image_raw', 10)
        self.subscription_ = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.cv_bridge_ = CvBridge()

    def image_callback(self, msg):
        # Convert the received image message to OpenCV format
        cv_image = self.cv_bridge_.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Perform any image processing here, if necessary
        cv2.imshow('Processed Image', cv_image)
        cv2.waitKey(1) 
        # Convert the processed image back to ROS Image message
        processed_image_msg = self.cv_bridge_.cv2_to_imgmsg(cv_image, encoding='bgr8')

        # Publish the processed image
        self.publisher_.publish(processed_image_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


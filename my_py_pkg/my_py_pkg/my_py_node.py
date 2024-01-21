#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Mynode(Node):

    def __init__(self):
        super().__init__("py_test_node")
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bool_value', rclpy.Parameter.Type.BOOL),
                ('int_value', rclpy.Parameter.Type.INTEGER),
                ('float_value', rclpy.Parameter.Type.DOUBLE),
                ('str_text', rclpy.Parameter.Type.STRING),
                ('bool_array', rclpy.Parameter.Type.BOOL_ARRAY),
                ('int_array', rclpy.Parameter.Type.INTEGER_ARRAY),
                ('float_array', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('str_array', rclpy.Parameter.Type.STRING_ARRAY),
                ('byte_array', rclpy.Parameter.Type.INTEGER_ARRAY),              
                ('nested_param.another_int', rclpy.Parameter.Type.INTEGER),
            ]
        )

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()
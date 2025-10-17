#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image

NODE_NAME = "cam_pub"

def publisher(img):
    if p != None:
        p.publish(img)

if __name__ == "__main__":
    rospy.init_node(NODE_NAME, log_level = rospy.INFO)
   
    p = rospy.Publisher("my_topic", Image, queue_size = 1)
    s = rospy.Subscriber("/usb_cam/image_raw", Image, publisher)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

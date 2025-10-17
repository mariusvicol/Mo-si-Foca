#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image

NODE_NAME = "image_node"

def img_preprocess(img):
    frame = np.ndarray(shape=(img.height, img.width, 3), dtype=np.uint8, buffer=img.data)
    cv2_img= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Frame", cv2_img)
    cv2.waitKey(1)


def cleanup():
    cv2.destroyWindow("Frame");


if __name__ == "__main__":
    rospy.init_node(NODE_NAME, log_level = rospy.INFO)
    rospy.on_shutdown(cleanup)
    rospy.Subscriber("/usb_cam/image_raw", Image, img_preprocess)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

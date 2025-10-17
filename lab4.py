#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image

NODE_NAME = "image_node_pub"

def img_preprocess(img):
    frame = np.ndarray(shape=(img.height, img.width, 3), dtype=np.uint8, buffer=img.data)
    cv2_img= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2HSV)

    msk = cv2.inRange(hsv, np.array([110,50, 50]), np.array([130, 255, 255]))
    contours, _ = cv2.findContours(msk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    largest_contour = max(contours, key=cv2.contourArea)

    contour_frame = cv2_img.copy()
    
    (x,y), radius = cv2.minEnclosingCircle(largest_contour)
    center = (int(x), int(y))

    circle = cv2.circle(contour_frame, center, int(radius), [235, 90, 210], 4)

    cv2.imshow("Frame", circle)
    cv2.waitKey(1)


def cleanup():
    cv2.destroyWindow("Frame")


if __name__ == "__main__":
    rospy.init_node(NODE_NAME, log_level = rospy.INFO)
    rospy.on_shutdown(cleanup)
    rospy.Subscriber("/usb_cam/image_raw", Image, img_preprocess)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

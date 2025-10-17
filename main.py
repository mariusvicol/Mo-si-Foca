#!/usr/bin/env python3

import rospy

def f():
    print("A")

if __name__ == "__main__":
    rospy.init_node("MoFoca", log_level = rospy.INFO)
    rospy.on_shutdown(f)
    print("b")
    rospy.spin()


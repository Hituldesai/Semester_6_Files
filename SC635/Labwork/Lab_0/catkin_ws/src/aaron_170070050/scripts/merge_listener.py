#!/usr/bin/env python

import rospy
from std_msgs.msg import String
name = "TEXT"
roll = "NUM"

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def callback(data):
    global name
    global roll
    if (is_number(data.data[0])):
        roll = data.data
    else:
        name = data.data
    rospy.loginfo('%s_%s', name, roll)

def merge_listener():
    rospy.init_node('merge_listener', anonymous=True)
    rospy.Subscriber('merge_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    merge_listener()

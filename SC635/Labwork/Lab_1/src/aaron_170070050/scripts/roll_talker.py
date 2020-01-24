#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def roll_talker():
    pub2 = rospy.Publisher('merge_topic', String, queue_size=10)
    rospy.init_node('roll_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        roll_str = "170070050"
        rospy.loginfo(roll_str)
        pub2.publish(roll_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        roll_talker()
    except rospy.ROSInterruptException:
        pass

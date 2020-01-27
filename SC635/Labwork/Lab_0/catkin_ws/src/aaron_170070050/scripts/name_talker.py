#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def name_talker():
    pub1 = rospy.Publisher('merge_topic', String, queue_size=10)
    rospy.init_node('name_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        name_str = "Aaron"
        rospy.loginfo(name_str)
        pub1.publish(name_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        name_talker()
    except rospy.ROSInterruptException:
        pass

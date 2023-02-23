#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64



def arm_init():
    
    rospy.init_node('arm_init')
    rate = rospy.Rate(1)
    topics = ['/joint_1', '/joint_2', '/joint_3', '/joint_4', '/joint_5']
    data = 0.0

    for topic in topics:
        pub = rospy.Publisher(topic + '/command', Float64, queue_size=10)
        pub.publish(data)
        rate.sleep()


 
if __name__=='__main__':
    
    try:
        arm_init()
    
    except rospy.ROSInterruptException:
        pass



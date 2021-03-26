#!/usr/bin/env python3



import rospy
from std_msgs.msg import String

def process_hello_world_msg(data):
    print("Message Recieved " + str(data))

def create_susbscriber():
    rospy.init_node("hello_world_sub_node")
    rospy.Subscriber("hello_world", String, process_hello_world_msg)

if __name__ == '__main__':
    create_susbscriber()
    rospy.spin()


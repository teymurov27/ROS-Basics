#!/usr/bin/env python3



import rospy
from std_msgs.msg import Float32

wheel_radius = 12.5 / 100 # Wheel Radius of robot in meters

def calc_speed(rpm, publisher):
    speed = rpm.data * 2 * 3.14159 / 60 * wheel_radius # speed in m/s
    publisher.publish(speed)

def create_susbscriber(pub):
    rospy.Subscriber("rpm", Float32, calc_speed, (pub))

if __name__ == '__main__':
    rospy.init_node("speed_calc_sub_node")
    pub = rospy.Publisher("speed", Float32, queue_size=10)
    create_susbscriber(pub)
    rospy.spin()


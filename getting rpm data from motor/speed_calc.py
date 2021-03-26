#!/usr/bin/env python3



import rospy
from std_msgs.msg import Float32

wheel_radius = rospy.get_param("/wheel_radius") # Wheel Radius of robot in meters

def calc_speed(rpm, publisher):
    wheel_radius = rospy.get_param("/wheel_radius")
    speed = rpm.data * 2 * 3.14159 / 60 * wheel_radius # speed in m/s
    publisher.publish(speed)

def create_susbscriber(pub):
    rospy.Subscriber("rpm", Float32, calc_speed, (pub))

if __name__ == '__main__':
    rospy.init_node("speed_calc_sub_node")
    pub = pub = rospy.Publisher("speed", Float32, queue_size=10)
    create_susbscriber(pub)
    rospy.spin()

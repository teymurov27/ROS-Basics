import rospy
from std_msgs.msg import Float32, String
from numpy import random

random.seed(None)
rpm_num = random.randint(low = 50, high = 99, size = (1, 1))


def rpm_pub():
    rospy.init_node("rpm_pub_node")
    pub = rospy.Publisher("rpm", Float32, queue_size=10)

    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        pub.publish(rpm_num)
        rate.sleep()

if __name__ == '__main__':
    try:
        rpm_pub()

    except rospy.ROSInterruptException:
        pass


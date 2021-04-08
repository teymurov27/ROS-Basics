#! /usr/bin/env python3



import math
import rospy
import actionlib

from udemy_pkg.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass:
    def __init__(self):
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, \
                                self.navigate_cb)

        self.robot_point_sub = rospy.Subscriber("robot/point", Point, self.update_robot_position)

        self.robot_current_point = None
        self.robot_goal_point = None
        self.distance_threshold = 0.25
        self.feedback_rate = rospy.Rate(1)

    def navigate_cb(self, goal):
        navigate_start_time = rospy.get_time()
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

        while self.robot_current_point == None and not rospy.is_shutdown():
            print("Robot Point Not Detected")
            rospy.sleep(5)

        print("Robot Point Detected")

        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        while distance_to_goal > self.distance_threshold:
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            self.feedback_rate.sleep()
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        navigate_end_time = rospy.get_time()

        elapsed_time = navigate_end_time - navigate_start_time

        rospy.loginfo("Navigation Successful, Elapsed Time: " + str(elapsed_time) + " seconds")
        self.action_server.set_succeeded(Navigate2DResult(elapsed_time))


    def update_robot_position(self, point):
        self.robot_current_point = [point.x, point.y, point.z]



if __name__ == "__main__":

    rospy.init_node("navigate_2D_action_server_node")
    server = Navigate2DClass()
    rospy.spin()


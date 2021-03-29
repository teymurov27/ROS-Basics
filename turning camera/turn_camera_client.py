#!/usr/bin/env python3



import rospy
from udemy_pkg.srv import TurnCamera, TurnCameraResponse

import os
import cv2
from cv_bridge import CvBridge

def configure_request(angle):
    rospy.wait_for_service("turn_camera")
    try:
        service_proxy = rospy.ServiceProxy("turn_camera", TurnCamera)
        resp_msg = service_proxy(angle)

        image_msg = resp_msg.image

        image = CvBridge().imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        cv2.imshow("Turn Camera Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except rospy.ServiceException as e:
        print("Service Request Failed: \n")
        print(e)


if __name__ == '__main__':
    try:
        rospy.init_node("turn_camera_client_node")
        user_input = input("\nEnter a angle in degrees to move robot camera: ")

        while user_input != "q":
            try:
                configure_request(float(user_input))
                user_input = input("\nEnter a angle in degrees to move robot camera: ")
            except:
                print("Error trying to process request")


    except rospy.ROSInterruptException:
        pass

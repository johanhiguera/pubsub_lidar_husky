#!/usr/bin/python

import rospy
from class_pubsub import LIDAR_RYCSV

# Init of program
if __name__ == '__main__':

    rospy.init_node('nodo_rycsv', anonymous=True)

    rospy.loginfo("Node init")

    LIDAR_RYCSV()

    rospy.spin()
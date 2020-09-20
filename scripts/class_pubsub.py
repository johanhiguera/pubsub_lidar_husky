#!/usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan

import numpy as np
from rospy.numpy_msg import numpy_msg 

class LIDAR_RYCSV:
    
    def __init__(self):

        self.nameTopicSub = "/scan"
        self.nameTopicPub = "/scan_fixed"
        self.newMsg = LaserScan() # LaserScan msg

        # Subscribers
        rospy.Subscriber(self.nameTopicSub, numpy_msg(LaserScan), self.Lidar_Callback, queue_size=10 )

        # Publisher
        self.pub = rospy.Publisher(self.nameTopicPub, numpy_msg(LaserScan), queue_size=10)

        # Polling con callback
        rate = rospy.Rate(20) # 20 Hz

        while (not rospy.is_shutdown()):

            self.pub.publish(self.newMsg)
            rate.sleep()

    #--------------------------------------------------------------------------------------#
    # Callback o interrupcion
    def Lidar_Callback(self, lidar_scan):
        
        new_msgLaserScan = lidar_scan
        new_msgRanges    = lidar_scan.ranges.copy()

        #new_msgLaserScan.ranges > 10 m   == 0
        #new_msgLaserScan.ranges < 0.5 m  == 0

        new_msgLaserScan.ranges = new_msgRanges
        self.newMsg = new_msgLaserScan
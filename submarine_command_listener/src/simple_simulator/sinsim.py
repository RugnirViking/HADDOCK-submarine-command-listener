#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int16

def crying_orangutan(data):
    rospy.loginfo("I received PITCH" +str(data.data))

def crying_polar_bears(data):
    rospy.loginfo("I received ROLL" +str(data.data))

def crying_animals_in_general(data):
    rospy.loginfo("I received HEADING" +str(data.data))

def crying_mother_earth_in_general(data):
    rospy.loginfo("I received ALTITUDE" +str(data.data))

def start(name):
    rospy.init_node('python_sub_command_listeners', anonymous=True) # node is called 'python_simple_sub_simulator'

    rospy.Subscriber("pitch_control_input", Int16, crying_orangutan)
    rospy.Subscriber("roll_control_input", Int16, crying_polar_bears)
    rospy.Subscriber("heading_control_input", Int16, crying_animals_in_general)
    rospy.Subscriber("altitude_control_input", Int16, crying_mother_earth_in_general)

    rate = rospy.Rate(50) # 50hz
    while not rospy.is_shutdown():

        rate.sleep()

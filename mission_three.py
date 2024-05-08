##########################################################
# Pybrcks Micropython Base Code For Lego Mindstorm EV3 
# Created in Partnership: FLL Team 18300 & Bolton Robotics
#
# This code is free for all to use and modify in the spirit 
# of co-opertition.  Please consider giving a shout-out to
# Bolton Robotics and FLL Team 18300 if you find it helpful.
#
##########################################################
# mission_three.py
##########################################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from bolton_robotics_robot import bolton_robotics_robot

def mission_three(r):
    r.ev3.screen.clear()
    print("Running Mission 3")
    r.ev3.screen.draw_text(30, 60, "Mission 3")
    wait(100)
    # The Best Mission! Aka, Emma's Mission! SLAY GIRLYPOP*instert MII theme*
    r.robot.straight(1500)
    r.robot.turn(-75)
    r.robot.straight(300)
    r.robot.turn(105)
    r.left_attachment_motor.run_angle(200, 180)
    r.robot.straight(-200)
    r.left_attachment_motor.run_angle(200, -180)
    r.robot.turn(90)
    r.robot.straight(100)
    r.robot.turn(90)
    r.robot.straight(-1500)
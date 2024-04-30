##########################################################
# Pybrcks Micropython Base Code For Lego Mindstorm EV3 
# Created in Partnership: FLL Team 18300 & Bolton Robotics
#
# This code is free for all to use and modify in the spirit 
# of co-opertition.  Please consider giving a shout-out to
# Bolton Robotics and FLL Team 18300 if you find it helpful.
#
##########################################################
# mission_one.py
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

def mission_one(r):
    r.ev3.screen.clear()
    print("Running Mission 1")
    r.ev3.screen.draw_text(30, 60, "Mission 1")
    wait(100)
    # Add your code below:
    r.robot.drive(300,-5)
    wait(2900)
    r.robot.stop()
    r.robot.drive(-330, 42.5)
    wait(1500)
    r.robot.stop()
    r.robot.straight(400)
    r.robot.straight(-200)
    r.robot.drive(150, -30)
    wait(500)
    r.robot.stop()
    r.left_attachment_motor.run_time(150, 2000)
    r.left_attachment_motor.run_time(-50, 250)
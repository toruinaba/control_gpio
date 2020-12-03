#!/usr/bin/env python

import time
from control_gpio.srv import *
import rospy

import RPi.GPIO as GPIO

def handle_single_gpio(req):
    if req.mode == "INIT":
        msg = "Initialize CH %s"%(req.ch)
        GPIO.setup(req.ch, GPIO.OUT, initial=GPIO.LOW)
    elif req.mode == "CLEAN":
        msg = "CLEANUP"
        GPIO.cleanup()
    elif req.mode == "OPEN":
        msg = "OPEN CH %s"%(req.ch)
        GPIO.output(req.ch, GPIO.HIGH)
    elif req.mode == "CLOSE":
        msg = "CLOSE CH %s"%(req.ch)
        GPIO.output(req.ch, GPIO.LOW)
    else:
        msg = "INVALID MODE"
    print msg
    return SingleGPIOResponse(msg)


def single_gpio_server():
    rospy.init_node('single_gpio_server')
    s = rospy.Service('single_gpio', SingleGPIO, handle_single_gpio)
    print "Ready to handle single GPIO"
    rospy.spin()

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    try:
        single_gpio_server()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
        GPIO.cleanup()


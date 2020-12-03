#!/usr/bin/env python

import sys
import rospy
from control_gpio.srv import *

def single_gpio_client(mode, ch):
    rospy.wait_for_service('single_gpio')
    try:
        handle_single_gpio = rospy.ServiceProxy('single_gpio', SingleGPIO)
        resp1 = handle_single_gpio(mode, ch)
        return resp1.msg
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [mode ch]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        mode = sys.argv[1]
        ch = int(sys.argv[2])
    else:
        print usage()
        sys.exit()
    print "Requesting Mode: %s    CH: %s"%(mode, ch)
    print "%s"%(single_gpio_client(mode, ch))


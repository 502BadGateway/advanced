#Sam wrote this!

from Tkinter import *
import time
import random


def invalid(robot, x,y):        #If the obstacle referance was invalid then bail out, because something went wrong in the generation.
    print "Invalid obstacle referance. Something went wrong, bailing out..."
    quit()

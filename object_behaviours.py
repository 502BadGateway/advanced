#Sam wrote this!

from Tkinter import *
import time
import random


def invalid(robot, x,y):        #If the obstacle referance was invalid then bail out, because something went wrong in the generation.
    print "Invalid obstacle referance. Something went wrong, bailing out..."
    quit()

def regular (robot, x,y):       #If there is a regular object the turn to a random direction 
    random_direction()
    return

def large (robot, x,y):         #Pretty much the same as the regular object. we dont need to behave any differently really.
    random_direction()
    return

def light (robot, x,y):
    #TODO Can't do this yet, waiting on Phil to impliment traffic light things.
    return


def mud (robot, x, y):
    decrease_speed()
    return

def boost(robot, x,y):
    increase_speed()
    return



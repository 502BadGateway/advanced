#Sam wrote this!

from Tkinter import *
import time
import random
import robot


def invalid(bot, direction,  x,y):        #If the obstacle referance was invalid then bail out, because something went wrong in the generation.
    print "Invalid obstacle referance. Something went wrong, bailing out..."
    quit()

def regular (bot, direction, x,y):       #If there is a regular object the turn to a random direction 
    robot.random_direction(direction)
    return

def large (bot, direction,  x,y):         #Pretty much the same as the regular object. we dont need to behave any differently really.
    robot.random_direction(direction)
    return

def light (bot, direction,  x,y):
    #generation_algorithim.generate_red_traffic_light(direction)
    #TODO Can't do this yet, waiting on Phil to impliment traffic light things.
    return


def mud (bot, direction,  x, y):
    robot.decrease_speed()
    return

def boost(bot, direction,  x,y):
    robot.increase_speed()
    return



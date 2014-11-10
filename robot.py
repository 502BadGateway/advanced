from Tkinter import *
import time
import random



def increase_speed():       #Increases the speed
    speed = speed *2
    return speed            #Yes speed is a global, but it might be easier in the future if we return something.

def decrease_speed():
    speed = speed /2
    return speed

def random_direction(direction):        #Chooses a random direction for the robot. Considers a given direction if given.
    new_direction = random.randint(0,4)

    if new_direction == direction:     #If we managed to choose the direction it said not too, choose another.
        random_direction(direction)
    else:
        return new_direction

def spawn_robot(arena):                  #Chooses a random place to spawn the robot.
   x_coord0 = random.randint(0,24)
   y_coord0 = random.randint(0,24)
   x_coord1 = x_coord0 + 20
   y_coord1 = y_coord0 + 20
   if arena_list[x_coord0 * 20][y_coord0*20] != 0:
       spawn_robot()
   else:
	robot = arena.create_oval(x_coord0, y_coord0, x_coord1, y_coord1, outline="green", fill="green", width=1)





def check(direction, x, y):


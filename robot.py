#Sam B Wrote this :D

#Robot directions:
#           0
#           ^
#           |
#       3 <- -> 1
#           |
#           V
#           2
#




from Tkinter import *
import time
import random
import object_behaviours



def increase_speed1():       #Increases the speed1
    speed11 = speed11 *2
    return speed11            #Yes speed1 is a global, but it might be easier in the future if we return something.

def decrease_speed1():
    speed1 = speed1 /2
    return speed1

def random_direction(direction):        #Chooses a random direction for the robot. Considers a given direction if given.
    new_direction = random.randint(0,3)

    if new_direction == direction:     #If we managed to choose the direction it said not too, choose another.
        random_direction(direction)
    else:
        return new_direction

def spawn_robot(arena):                  #Chooses a random place to spawn the robot.
    x_coord0 = random.randint(0,24)
    y_coord0 = random.randint(0,24)
    x_coord1 = x_coord0 + 20
    y_coord1 = y_coord0 + 20
    if arena_list[x_coord0 * 20][y_coord0*20] != 0:      #If there is something in the element. Dont spawn there.
        spawn_robot()
    else:
        robot = arena.create_oval(x_coord0, y_coord0, x_coord1, y_coord1, outline="green", fill="green", width=1)
return robot                            #Returns Robot ID for moving it.


options {                   #Dictionary containing the object numbers and the functions assotiated with them.
        0:invalid,          #All these functions are defined in object_behaviours.py
        1:regular,
        2:large,
        3:light,
        4:mud,
        5:boost
        }

def check(direction, x, y):
    if direction == 0:    # If the direction is upward...  
        check_y = (y /20) - 1
        check_x = (x /20) #Then check upward!
        if arena_list[check_x][check_y] != 0:
            options[arena_list[check_x][check_y] ()
        else:
        return
    if direction == 1:    # If the direction is right...  
        check_y = (y /20) 
        check_x = (x /20) + 1 #Then check right!
        if arena_list[check_x][check_y] != 0:
            options[arena_list[check_x][check_y] ()
        else:
        return
    if direction == 2:    # If the direction is right...  
        check_y = (y /20) + 1 
        check_x = (x /20) #Then check right!
        if arena_list[check_x][check_y] != 0:
            options[arena_list[check_x][check_y] ()
        else:
        return
    if direction == 3:    # If the direction is right...  
        check_y = (y /20)  
        check_x = (x /20) - 1 #Then check right!
        if arena_list[check_x][check_y] != 0:
            options[arena_list[check_x][check_y] ()
        else:
        return
        

def move(robot,direction,  arena):   #Moves the robot
    if direction == 0:
        arena.move(robot, 0, -20)
    elif direction == 1:
        arena.move(robot, 20, 0)
   elif direction == 2:
        arena.move(robot, 0, 20)
   elif direction == 3:
        arena.move(robot, -20, 0)

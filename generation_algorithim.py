from Tkinter import *
import time
import random
import robot

#block bellow checks for what OS the user is using and if it is Darwin (OSX) then it increases the speed, this is to fix the issue of the robot being very slow on OSX
import platform
platform_name=platform.system()
print platform_name
if platform_name == "Darwin":
    speed=0.001
else:
    speed=0.01
print speed

"""
Below is a multi-dimensional list of lists. It is essentially 25 lists constaining 25 elements. 
This gives us a direct reference to a grid of 25x25. 
Due to the fact our arena is 500px by 500px it means each element represents a 20px x 20px area.
We can reference any area using the notation "arena_list[x][y] and access the stuff inside.
"""
arena_list = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    						 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
"""
Below is the function to randomly generate a object. 
The majority of obstacles are generated the same way, just with different conditions.
This will randomly pick two numbers between 0 and 24, which are saved into two different variables (x_list and y_list).
We use these variables to access the list using arena_list[x_list][y_list]
We then check if that element is empty (or "0")
If it isn't, we simple run the function again from the top, trying a different spot. 
If it is, we change it to a number, to represent the object which is now in that area.
We then use those two variables to create an object on the Tkinter GUI.
This works because x_list/y_list x 20 is actually the coords on the window for the object. 
e.g. x_list = 6 and y_list = 10 means that we have the coords on canvas 120 x 200. 
Using this top corner, we generate the rest of the coords, by adding 20.
Finally we generate an object using the coords we created using the x_list and y_list numbers.
"""
def generate_obstacle(arena_list, arena):
    	x_list = random.randint(0,24)           #
    	y_list = random.randint(0,24)
    	if(arena_list[x_list][y_list] == 0):
    			arena_list[x_list][y_list] = 1
    			x_coord0 = x_list * 20
    			y_coord0 = y_list * 20
    			x_coord1 = x_coord0 + 20
    			y_coord1 = y_coord0 + 20
    			obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "red", outline = "black")
    			
    	else:
    			generate_obstacle(arena_list, arena)
    	return arena_list

def generate_big_obstacle(arena_list, arena):
    	x_list = random.randint(0,24)
    	y_list = random.randint(0,24)
    	if(x_list < 23 and y_list < 23 and arena_list[x_list][y_list] == 0 and arena_list[x_list + 1][y_list] == 0 and arena_list[x_list][y_list + 1] == 0 and arena_list[x_list + 1][y_list + 1] == 0):
    			arena_list[x_list][y_list] = 2
    			arena_list[x_list + 1][y_list] = 2
    			arena_list[x_list][y_list + 1] = 2
    			arena_list[x_list + 1][y_list + 1] = 2
    			x_coord0 = x_list * 20
    			y_coord0 = y_list * 20
    			x_coord1 = x_coord0 + 40
    			y_coord1 = y_coord0 + 40
    			obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "green", outline = "black")
    			arena.update()
    			time.sleep(0.1)
    	else:
    			generate_big_obstacle(arena_list, arena)
    	return arena_list
def generate_traffic_light_object(arena_list,arena):
    print "traffics light"
    x_list = random.randint(0,24)
    y_list = random.randint(0,24)
    if (arena_list[x_list][y_list] == 0):
    	arena_list[x_list][y_list] = 3
    	arena_list[x_list + 1][y_list] = 3
    	arena_list[x_list + 2][y_list] = 3
    	x_coord0 = x_list * 20
    	y_coord0 = y_list * 20
    	x_coord1 = x_coord0 + 60
    	y_coord1 = y_coord0 + 20
    	obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "pink")
    	arena.update()
    else:
    	generate_traffic_light_object(arena_list,arena)
def generate_mud_object(arena_list,arena):
    print "mud"
    x_list = random.randint(0,24)
    y_list = random.randint(0,24)
    if(x_list < 23 and y_list < 23 and arena_list[x_list][y_list] == 0 and arena_list[x_list + 1][y_list] == 0 and arena_list[x_list][y_list + 1] == 0 and arena_list[x_list + 1][y_list + 1] == 0):
    		arena_list[x_list][y_list] = 4
    		arena_list[x_list + 1][y_list] = 4
    		arena_list[x_list][y_list + 1] = 4
    		arena_list[x_list + 1][y_list + 1] = 3
    		x_coord0 = x_list * 20
    		y_coord0 = y_list * 20
    		x_coord1 = x_coord0 + 40
    		y_coord1 = y_coord0 + 40
    		obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "brown", outline = "black")
    		arena.update()
    		time.sleep(0.1)
    else:
    	generate_mud_object(arena_list,arena)
def generate_speed_boost_object(arena_list,arena):
    print "speed boost"
    x_list = random.randint(0,24)
    y_list = random.randint(0,24)
    if (arena_list[x_list][y_list] == 0):
    	arena_list[x_list][y_list] = 5
    	x_coord0 = x_list * 20
    	y_coord0 = y_list * 20
    	x_coord1 = x_coord0 + 20
    	y_coord1 = x_coord0 + 20
    	obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "orange", outline = "black")
    	arena.update()
    else:
    	generate_speed_boost_object(arena_list,arena)
def advanced_init():
    	window2 = Tk()
    	arena = Canvas(window2, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
    	for i in range(0,30):
    		generate_obstacle(arena_list, arena)
    		arena.update()
    	

    	for i in range(0,5):
    		generate_big_obstacle(arena_list, arena)
    		arena.update()

    	for i in range(0,3):
    		generate_traffic_light_object(arena_list,arena)
    		arena.update()


        robot.spawn_robot(arena)


    	for i in range(0,3):
    		generate_mud_object(arena_list,arena)
    		arena.update()

    	for i in range(0,3):
    		generate_speed_boost_object(arena_list,arena)
    		arena.update()

    	print arena_list
        

    	arena.pack()

    	arena.update_idletasks()
    	speed=0.1

    	window2.mainloop() # runs everything






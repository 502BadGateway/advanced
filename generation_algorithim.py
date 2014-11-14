from Tkinter import *
import time
import random
#import gc
#gc.disable()
#block bellow checks for what OS the user is using and if it is Darwin (OSX) then it increases the speed, this is to fix the issue of the robot being very slow on OSX
import platform
platform_name=platform.system()
print platform_name
if platform_name == "Darwin":
	speed1=0.001
	speed2=0.001
else:
	speed2=0.01
	speed2=0.01

print speed2

traffic_list=[]
global call_num
call_num=1
global obstacle


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
		x_list = random.randint(0,24)           
		y_list = random.randint(0,24)
		if(arena_list[x_list][y_list] == 0):
				arena_list[x_list][y_list] = 1
				x_coord0 = x_list * 20
				y_coord0 = y_list * 20
				x_coord1 = x_coord0 + 20
				y_coord1 = y_coord0 + 20
				global small_obstacle
				small_obstacle = PhotoImage(file = 'obstacle.gif')
				obstacle = arena.create_image(x_coord0, y_coord0, image = small_obstacle, anchor = NW)
				arena.update()
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
				global big_obstacle
				big_obstacle = PhotoImage(file = 'obstacle.gif')
				obstacle = arena.create_image(x_coord0, y_coord0, image = big_obstacle, anchor = NW)
				arena.update()
				time.sleep(0.1)
		else:
				generate_big_obstacle(arena_list, arena)
		return arena_list
def generate_traffic_light_object(arena_list,arena,traffic_list):
	print "traffics light"
	x_list = random.randint(0,24)
	y_list = random.randint(0,24)
	traffic_list.append(x_list)
	traffic_list.append(y_list)
	if (x_list< 22 and arena_list[x_list][y_list] == 0):
		arena_list[x_list][y_list] = 3
		arena_list[x_list + 1][y_list] = 3
		arena_list[x_list + 2][y_list] = 3
		x_coord0 = x_list * 20
		y_coord0 = y_list * 20
		x_coord1 = x_coord0 + 60
		y_coord1 = y_coord0 + 20
		global traffic_light_green_obstacle
		traffic_light_green_obstacle = PhotoImage(file = 'traffic_light_green.gif')
		obstacle = arena.create_image(x_coord0, y_coord0, image = traffic_light_green_obstacle, anchor = NW)
		arena.update()
	else:
		generate_traffic_light_object(arena_list,arena,traffic_list)
	
def generate_mud_object(arena_list,arena):
	print "mud"
	x_list = random.randint(0,24)
	y_list = random.randint(0,24)
	if(x_list < 23 and y_list < 23 and arena_list[x_list][y_list] == 0 and arena_list[x_list + 1][y_list] == 0 and arena_list[x_list][y_list + 1] == 0 and arena_list[x_list + 1][y_list + 1] == 0):
			arena_list[x_list][y_list] = 4
			arena_list[x_list + 1][y_list] = 4
			arena_list[x_list][y_list + 1] = 4
			arena_list[x_list + 1][y_list + 1] = 4
			x_coord0 = x_list * 20
			y_coord0 = y_list * 20
			x_coord1 = x_coord0 + 40
			y_coord1 = y_coord0 + 40
			global mud_obstacle
			mud_obstacle = PhotoImage(file = 'mud.gif')
			obsactle = arena.create_image(x_coord0, y_coord0, image = mud_obstacle, anchor = NW)
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
		y_coord1 = y_coord0 + 20
		global speed_boost_obstacle
		speed_boost_obstacle = PhotoImage(file = 'speed_boost.gif')
		obstacle = arena.create_image(x_coord0, y_coord0, image = speed_boost_obstacle, anchor = NW)
 
		arena.update()
	else:
		generate_speed_boost_object(arena_list,arena)
def genertate_red_traffic_light(arena_list,arena): # this function gives the traffic light locations and it turns the traffic light red
	print "red"
	if call_num == 1:
		traffic_x_coord0 = traffic_list[1]
		traffic_y_coord0 = traffic_list[2]

		traffic_light_change(traffic_x_coord0,traffic_y_coord0)
	elif call_num == 2:
		traffic_x_coord0 = traffic_list[3]
		traffic_y_coord0 = traffic_list[4]
	elif call_num == 3:
		traffic_x_coord0 = traffic_list[5]
		traffic_y_coord0 = traffic_list[6]
	else:
		print "no more in list"

	call_num = call_num + 1
def traffic_light_change(traffic_x_coord0,traffic_y_coord0):
	traffic_x_coord1 = traffic_x_coord0 + 1
	traffic_y_coord1 = traffic_y_coord0 + 1

	global traffic_light_red
	traffic_light_red = PhotoImage(file = 'traddif_light_red.gif')
	obstacle = arena.create_image(traffic_x_coord0, traffic_y_coord0, image = traffic_light_red, anchor = NW)
	# we could either do a pause or change robot speed to 0 here 
	arena.delete(obstacle_red_traffic)
	arena.update()
def generate_finish_area():
	x_list = random.randint(0,24)
	y_list = random.randint(0,24)
	if (arena_list[x_list][y_list] == 0):
		arena_list[x_list][y_list] = 7
		x_coord0 = x_list * 20
		y_coord0 = y_list * 20
		x_coord1 = x_coord0 + 20
		y_coord1 = y_coord0 + 20

def advanced_init():
		window2 = Toplevel()
		arena = Canvas(window2, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
		for i in range(0,5):
			generate_big_obstacle(arena_list, arena)
			arena.update()
		for i in range(0,3):
			generate_mud_object(arena_list,arena)
			arena.update()
		for i in range(0,3):
			generate_traffic_light_object(arena_list,arena,traffic_list)
			arena.update()
		for i in range(0,3):
			generate_speed_boost_object(arena_list,arena)
			arena.update()
		for i in range(0,30):
			generate_obstacle(arena_list, arena)
			arena.update()
		print arena_list

		import robot

		robot1 = robot.Robot()
		robot1.speed = speed2
		robot1.spawn_robot(arena)
		# robot1.spawn_robot(robot1,arena)
		print arena_list
		
		direction = 0

		arena.pack()
		arena.update()
		arena.update_idletasks()
		go = True

		while go == True:
			print go
			print  arena.coords(robot1)
			if robot1.coords[2] >= 480:
				print "hit a wall first"
				robot1.random_direction(robot1.direction)
				robot1.move(arena)
			elif robot1.coords[0] < 20:
				print "hit a wall second"
				robot1.random_direction(robot1.direction)
				robot1.move(arena)
			elif robot1.coords[1] >= 480:
				print "hit a wall third"
				robot1.random_direction(robot1.direction)
				robot1.move(arena)
			elif robot1.coords[1] <= 20:
				print "hit a wall fourth"
				robot1.random_direction(robot1.direction)
				robot1.move(arena)
			robot1.check()
			robot1.move(arena)
			arena.update()
			time.sleep(0.1)
		print  arena.coords(robot1)
		print go
		global speed_boost_obstacle
		"""
		speed_boost_obstacle = PhotoImage(file = 'speed_boost.gif')
		arena.create_image(10, 10, image = speed_boost_obstacle, anchor = NW)
		arena.pack()
		arena.update()
		print " this is a test"
		"""
		robot.direction = direction
		window2.mainloop() # runs everything



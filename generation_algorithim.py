from Tkinter import *
import time
import random

#block bellow checks for what OS the user is using and if it is Darwin (OSX) then it increases the speed, this is to fix the issue of the robot being very slow on OSX
import platform
platform_name=platform.system()
print platform_name
if platform_name == "Darwin":
	speed=0.001
else:
	speed=0.01
print speed
traffic_list=[]
global 	call_num
call_num=1
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

def generate_obstacle(arena_list, arena):
		x_list = random.randint(0,24)           #
		y_list = random.randint(0,24)
		if(arena_list[x_list][y_list] == 0):
				arena_list[x_list][y_list] = 1
				x_coord0 = x_list * 20
				y_coord0 = y_list * 20
				x_coord1 = x_coord0 + 20
				y_coord1 = y_coord0 + 20
				obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "blue", outline = "black")
				
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
				obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "blue", outline = "black")
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
		x_coord1 = x_coord0 + 20
		y_coord1 = y_coord0 + 20
		obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "green")
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
			obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "brown", outline = "brown")
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
		obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "orange", outline = "green")

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

	obstacle_red_traffic = arena.create_rectangle(traffic_x_coord0, traffic_y_coord0, traffic_x_coord1, traffic_y_coord1, fill = "red", outline = "black")
	 
	arena.delete(obstacle_red_traffic)
	arena.update()
def advanced_init():
		window2 = Tk()
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

		arena.pack()

		arena.update_idletasks()
		speed=0.1

		window2.mainloop() # runs everything







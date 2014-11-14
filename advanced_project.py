#!/usr/bin/env python
from Tkinter import *
import time # imports the time moduale
import random
import generation_algorithim


def traffic_light(arena,key_panel): #Danny
		traffic_light = random.randint(0,1000)
		if (traffic_light < 5):
			global key_panel2
			key_panel2 = PhotoImage(file = 'advance_key_red.gif')
			arena.create_image(0,735, image = key_panel2, anchor = SW)
			#Change traffic_light.gif_green to traffic_light_red.gif
			print "RED!"
			arena.update()

			time.sleep(5)
			print "GREEN!"
			global key_panel3
			key_panel3 = PhotoImage(file = 'advance_key_green.gif')
			arena.create_image(0,735, image = key_panel3, anchor = SW)
			arena.update()
			
def basic():
	window2 = Toplevel()
	arena = Canvas(window2, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena

	obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red", outline = "red") # creates a obstacle to avoid
	obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red", outline = "red")
	obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red", outline = "red")
	obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red", outline = "red")
	obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red", outline = "red")
	obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red", outline = "red")
	start_arena = arena.create_rectangle(0, 450, 50, 500, fill = "#82FA02") # uses a Hexidecimal code for light green

	#flag gif
	gif1 = PhotoImage(file = 'flag.gif')
	arena.create_image(500, 0, image = gif1, anchor = NE,)

	#create triangle robot
	#robot = arena.create_polygon([(10, 450), (10, 500), (40, 475)], fill="#366605")
	robot = arena.create_oval(50, 500, 30, 480, outline="green", fill="green", width=1)
	arena.pack()

	arena.update_idletasks()
	speed1=0.1
	for t in range(0,450):
		arena.move(robot , 1 , 0)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0 , -0.335)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , -0.8 , 0)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0 , -0.4)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0.42 , 0)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0 , 0.155)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0.35 , 0)
		arena.update()
		time.sleep(speed1)
	for t in range(0,450):
		arena.move(robot , 0 , -0.45)
		arena.update()
		time.sleep(speed1)
	#robot_front, robot_back1, robot_back2 = arena.coords(robot)
	#print robot_front
	window2.mainloop() # runs everything
window1= Tk()
def intermdiate():
	window2 = Toplevel()
	arena = Canvas(window2, width = 500, height = 735, bg = 'white') # generates a canvas of 500px x 500px for the arena
	#key = Canvas(window2, width =  500, height = 200, bg = "grey")# generates the panel the key is on

	obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red", outline = "black") # creates a obstacle to avoid
	obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red", outline = "black")
	obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red", outline = "black")
	obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red", outline = "black")
	obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red", outline = "black")
	obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red", outline = "black")
	start_arena = arena.create_rectangle(0, 450, 50, 500, fill = "#82FA02") # uses a Hexidecimal code for light green

	arena.pack()
	speed1=0.01
	robot = arena.create_oval(50, 500, 30, 480, outline="black", fill="darkgreen", width=1)

	random_number=random.randint(0,6) 
	gif1 = PhotoImage(file = 'flag.gif')
	arena.create_image(500, 0, image = gif1, anchor = NE,)
	key_panel = PhotoImage(file = 'advance_key_green.gif')
	arena.create_image(0,735, image = key_panel, anchor = SW)

	
	if random_number==1:
		print "1"
		for t in range(0,450): #route by ade
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0 , -0.335)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , -0.8 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0 , -0.4)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0.42 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0 , 0.155)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0.35 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot , 0 , -0.45)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
	elif random_number==2:
		print "2"
		for t in range(0,450): # route by phil
			arena.move(robot ,0.7 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot ,0 , -0.57)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot,0.3,0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,450):
			arena.move(robot, 0, -0.48)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

	elif random_number==3:
		print "3"
		for t in range(0,300): #route by fami
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,200):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,210):
			arena.move(robot , -1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,250):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,350):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
	elif random_number==4:
		print "4"
		for t in range(0,280):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,320):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,200):
			arena.move(robot , -1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,100):
			arena.move(robot , 0 , 1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,230):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,50):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,130):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,190):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

	elif random_number==5: #Dannys Route
		print "5"
		for t in range(0,280):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,320):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,200):
			arena.move(robot , -1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,150):
			arena.move(robot , 0 , 1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,350):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,100):
			arena.move(robot , 0 , 1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
		for t in range(0,150):
			arena.move(robot , -1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

		for t in range(0,400):
			arena.move(robot , 0 , -1)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,160):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
	elif random_number==6: #route byb ade
		print "6"
		for t in range(0,450):
			arena.move(robot , 1 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , -0.35)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.3 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , -0.23)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.14 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , -0.45)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.2 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , 0.55)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.45 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , -0.2)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.475 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.06 , 0.09)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.17 , 0.09)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.28 , 0.2)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.28 , -0.2)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , -0.17 , -0.09)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.06 , -0.09)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , 0.09)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0.3 , 0)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)
			
		for t in range(0,450):
			arena.move(robot , 0 , -0.44)
			arena.update()
			time.sleep(speed1)
			traffic_light(arena,key_panel)

#key = Canvas(window, width = 500, height = 100, bg = 'grey') # generates a canvas for our key and UI area
#key.pack()
def callback_basic(): # calls the basic function when the user clicks the button
	basic()
def callback_intermediate(): # calls the intermediate function  when user clicks the button 
	intermdiate() 
def callback_advanced():
	generation_algorithim.advanced_init()
c = Button(window1, text="Advanced", command=callback_advanced) # creates a button that will take the user to the advanced task
c.pack(side=RIGHT)
b = Button(window1, text="Intermediate", command=callback_intermediate) #  creates a button that will take the user to the intermediate task
b.pack(side=RIGHT)
a = Button(window1, text="Basic", command=callback_basic) # creates a button that will take the user to the basic task
a.pack(side=RIGHT)

mainloop()
window2 = Tk()
arena = Canvas(window2, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena

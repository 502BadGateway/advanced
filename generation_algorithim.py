from Tkinter import *
import time # imports the time moduale
import random

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
window2 = Tk()
arena = Canvas(window2, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena

def generate_obstacle(arena_list):
    x_list = random.randint(0,24)
    y_list = random.randint(0,24)
    if(arena_list[x_list][y_list] == 0):
        arena_list[x_list][y_list] = 1
        x_coord0 = x_list * 20
        y_coord0 = y_list * 20
        x_coord1 = x_coord0 + 20
        y_coord1 = y_coord0 + 20
        obstacle = arena.create_rectangle(x_coord0, y_coord0, x_coord1, y_coord1, fill = "red", outline = "black")
        
    else:
        generate_obstacle(arena_list)
    return arena_list

def generate_big_obstacle(arena_list):
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
        
    else:
        generate_big_obstacle(arena_list)
    return arena_list


for i in range(0,50):
    generate_obstacle(arena_list)
    time.sleep(0.5)
    arena.update()

for i in range(0,5):
    generate_big_obstacle(arena_list)
    time.sleep(0.5)
    arena.update()

print arena_list

#robot = arena.create_oval(50, 500, 30, 480, outline="green", fill="green", width=1)
arena.pack()

arena.update_idletasks()
speed=0.1

window2.mainloop() # runs everything
#window1= Tk()

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
import generation_algorithim


class Robot:


    speed = 0
    direction = 0
    coords = []
    id = 0


    def __init__(self):
        self.direction = random.randint(0,3)
        return



    def invalid(self):        #If the obstacle referance was invalid then bail out, because something went wrong in the generation.
        return 

    def regular (self):       #If there is a regular object the turn to a random direction 
        self.random_direction(self.direction)
        return
    
    def large (self):         #Pretty much the same as the regular object. we dont need to behave any differently really.
        self.random_direction(self.direction)
        return
    
    def light (self):
        #TODO Can't do this yet, waiting on Phil to impliment traffic light things.
        return
    
    
    def mud (self):
        self.decrease_speed()
        return
    
    def boost(self):
        self.increase_speed()
        return


    def increase_speed(self):       #Increases the speed
        self.speed = self.speed*2
        return self.speed            #Yes speed is a global, but it might be easier in the future if we return something.
    
    def decrease_speed(self):
        self.speed = self.speed/2
        return self.speed
    
    def random_direction(self,direction):        #Chooses a random direction for the robot. Considers a given direction if given.
        new_direction = random.randint(0,3)
        print "new direction: "+str(new_direction)
        if new_direction == self.direction:     #If we managed to choose the direction it said not too, choose another.
            self.random_direction(self.direction)
        else:
            self.direction = new_direction
            return new_direction
    
    def spawn_robot(self,arena):                  #Chooses a random place to spawn the robot.
        x_list = random.randint(0,24)
        y_list = random.randint(0,24)
        x_coord0 = x_list * 20
        y_coord0 = y_list * 20
        x_coord1 = x_coord0 + 20 
        y_coord1 = y_coord0 + 20
        print len(generation_algorithim.arena_list)
        if generation_algorithim.arena_list[x_list][y_list] != 0:      #If there is something in the element. Dont spawn there.
           self.spawn_robot(arena)

        else:
            robot = arena.create_oval(x_coord0, y_coord0, x_coord1, y_coord1, outline="green", fill="green", width=1)
            self.coords = arena.coords(robot)
            print self.coords
            self.id = robot
        return                            #Returns Robot ID for moving it.
    
    
    
    def check(self):
        print self.coords
        if int(self.coords[1]) /20 -1 < 0 or int(self.coords[0]) /20 -1 < 0 or int(self.coords[1]) /20 +1 >= 25 or int(self.coords[0]) /20 +1 >= 25 :
            self.random_direction(self.direction)
            return
        if self.direction == 0:    # If the direction is upward...  
            check_y = (int(self.coords[1] /20))-1
            check_x = (int(self.coords[0] /20)) #Then check upward!
            print "checking upward..."
            print "check X:"+str(check_x)
            print "check Y:"+str(check_y)
            if generation_algorithim.arena_list[check_x][check_y] != 0: 
                if generation_algorithim.arena_list[check_x][check_y] == 1:
                    print "called regular"
                    self.regular()
                elif generation_algorithim.arena_list[check_x][check_y] == 2:
                    self.large()
                elif generation_algorithim.arena_list[check_x][check_y] == 3:
                    self.light()
                elif generation_algorithim.arena_list[check_x][check_y] == 4:
                    self.mud()
                elif generation_algorithim.arena_list[check_x][check_y] == 5:
                    self.boost()
            else:
                return
        elif self.direction == 1:    # If the direction is right...  
            check_y = (int(self.coords[1] /20)) 
            check_x = (int(self.coords[0] /20)) + 1 #Then check right!
            if generation_algorithim.arena_list[check_x][check_y] != 0: 
                if generation_algorithim.arena_list[check_x][check_y] == 1:
                    print "called regular"
                    self.regular()
                elif generation_algorithim.arena_list[check_x][check_y] == 2:
                    self.large()
                elif generation_algorithim.arena_list[check_x][check_y] == 3:
                    self.light()
                elif generation_algorithim.arena_list[check_x][check_y] == 4:
                    self.mud()
                elif generation_algorithim.arena_list[check_x][check_y] == 5:
                    self.boost()
            else:
                return
        elif self.direction == 2:    # If the direction is right...  
            check_y = (int(self.coords[1] /20)) + 1 
            check_x = (int(self.coords[0] /20)) #Then check right!
            if generation_algorithim.arena_list[check_x][check_y] != 0: 
                if generation_algorithim.arena_list[check_x][check_y] == 1:
                    print "called regular"
                    self.regular()
                elif generation_algorithim.arena_list[check_x][check_y] == 2:
                    self.large()
                elif generation_algorithim.arena_list[check_x][check_y] == 3:
                    self.light()
                elif generation_algorithim.arena_list[check_x][check_y] == 4:
                    self.mud()
                elif generation_algorithim.arena_list[check_x][check_y] == 5:
                    self.boost()
            else:
                return
        elif self.direction == 3:    # If the direction is right...  
            check_y = (int(self.coords[1] /20))  
            check_x = (int(self.coords[0] /20)) - 1 #Then check right!
            if generation_algorithim.arena_list[check_x][check_y] != 0: 
                if generation_algorithim.arena_list[check_x][check_y] == 1:
                    print "called regular"
                    self.regular()
                elif generation_algorithim.arena_list[check_x][check_y] == 2:
                    self.large()
                elif generation_algorithim.arena_list[check_x][check_y] == 3:
                    self.light()
                elif generation_algorithim.arena_list[check_x][check_y] == 4:
                    self.mud()
                elif generation_algorithim.arena_list[check_x][check_y] == 5:
                    self.boost()
            else:
                return
    
    
    def move(self,arena):   #Moves the robot 20 spaces to where ever the robot is pointing.
        if self.direction == 0:
            arena.move(self.id, 0, -20)
        elif self.direction == 1:
            arena.move(self.id, 20, 0)
        elif self.direction == 2:
            arena.move(self.id, 0, 20)
        elif self.direction == 3:
            arena.move(self.id, -20, 0)
        self.coords = arena.coords(self.id) 
        print "moved"


       

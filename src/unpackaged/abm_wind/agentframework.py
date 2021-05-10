# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:18:19 2021

@author: katie
"""

#agent framework for bacteria particles

import random

#variables

bomblocation = (150,50)
buildingheight = 75
fall_up_percent = 20
fall_down_percent = 70
fall_same_percent = 10

wind_north_percent = 10
wind_east_percent = 75
wind_south_percent = 10
wind_west_percent = 5

#create percentage values
n_per = wind_north_percent/100
e_per = wind_east_percent/100
s_per = wind_south_percent/100
w_per = wind_west_percent/100
up_per = fall_up_percent/100
d_per = fall_down_percent/100
same_per = fall_same_percent/100





class Particle():
    
    def __init__(self, environment):
        self.y = bomblocation[0]
        self.x = bomblocation[1]
        self.z = buildingheight
        self.environment = environment
        
    def move_fall(self):

        if random.random() < up_per:
            self.z += 1    
        elif random.random() > (up_per) and random.random() < (up_per + d_per):
            self.z -= 1        
        else:
            self.z += 0
     
        
    def move_nsew(self):
    
        if random.random() < n_per:
            self.y -= 1        
        elif random.random() > (n_per) and random.random() < (n_per + e_per):
            self.x += 1
        elif random.random() > n_per + e_per and random.random() < (n_per + e_per + s_per):
            self.y += 1            
        else:    
            self.x -= 1
            
          
    def settle(self):
        
        self.environment[self.y][self.x] += 1
            

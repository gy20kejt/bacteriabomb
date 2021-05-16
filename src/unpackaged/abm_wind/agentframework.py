# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:18:19 2021

@author: katie
"""

#agent framework for bacteria particles

import random

#variables

bomblocation = (150,50) #bomb location hardcoded in as unable to draw from model file
buildingheight = 75 # building height
fall_up_percent = 20 # percentage chance of particle rising.
fall_down_percent = 70 # percentage chance of particle falling
fall_same_percent = 10 # percentage chance of particle staying at same height

wind_north_percent = 10 #percentage chance wind blow north
wind_east_percent = 75 #percentage chance wind blow east
wind_south_percent = 10 #percentage chance wind blow south
wind_west_percent = 5 #percentage chance wind blow west

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
        """
        Create a new bacteria particle.

        Parameters:
        environment : The environment the particle will spawn in

        Returns:
        None
        """  
        self.y = bomblocation[0] # starting y coordinate
        self.x = bomblocation[1] # starting x coordinate
        self.z = buildingheight # starting z coordinate
        self.environment = environment
        

        
    def move_fall(self): # Function to make the particle move up or down
        """
        Makes a particle move up, down or stay the same height.

        Parameters:
        up_per (float): percentage chance divided by 100
        d_per (float): percentage chance divided by 100
        same_per (float): percentage chance divided by 100

        Returns:
        None
        """ 
        if random.random() < up_per: 
            self.z += 1    
        elif random.random() > (up_per) and random.random() < (up_per + d_per):
            self.z -= 1        
        else:
            self.z += 0
   
        
    def move_nsew(self): # Make the particle move in cardinal directions
        """
        Makes a particle move north, south, east or west.

        Parameters:
        n_per (float): percentage chance divided by 100
        e_per (float): percentage chance divided by 100
        s_per (float): percentage chance divided by 100

        Returns:
        None
        """  
        if random.random() < n_per:
            self.y -= 1        
        elif random.random() > (n_per) and random.random() < (n_per + e_per):
            self.x += 1
        elif random.random() > n_per + e_per and random.random() < (n_per + e_per + s_per):
            self.y += 1            
        else:    
            self.x -= 1
          
          
    def settle(self): #Add plus one to the environment array
        """
        Marks the environment array with plus one at particle location

        Parameters:
        environment: the environment the particle is spawned in.

        Returns:
        None
        """
        self.environment[self.y][self.x] += 1
            

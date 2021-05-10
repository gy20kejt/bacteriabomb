# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:11:35 2021

@author: katie
"""

#bacteria bomb tracking particle model

#import nesc modules

import csv
import matplotlib.pyplot
import random


#create empty lists
environment = []
agents = []


#create variables
buildingpos = 255
buildingheight = 75
number_particles = 100


fall_up_percent = 20
fall_down_percent = 70
fall_same_percent = 10

wind_north_percent = 10
wind_east_percent = 75
wind_south_percent = 10
wind_west_percent = 5

#create percentage values
north_percent = wind_north_percent/100
east_percent = wind_east_percent/100
south_percent = wind_south_percent/100
west_percent = wind_west_percent/100
up_percent = fall_up_percent/100
down_percent = fall_down_percent/100
same_percent = fall_same_percent/100

#populate environment from reading in raster file

bmap = open('wind.raster', newline='') 
reader = csv.reader(bmap, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:		
    rowlist = []   		
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist) 
bmap.close() 
   
#get building location coordinate from environment

bombloc = ([(index, row.index(buildingpos)) for index, row in enumerate(environment) 
       if buildingpos in row])

print(bombloc) # just to check there is a coordinate
bomb = (bombloc[0]) # since it was a tuple in the list
bomb_y = (bomb[0]) 
bomb_x = (bomb[1])
# bring up a plot of the environemt.  You can see the building dot at ~ 150,50
matplotlib.pyplot.imshow(environment)


# Make the Agents
for i in range(number_particles):
    agents.append([bomb_y, bomb_x, buildingheight])
#print(agents)

#Define functions to fall and move.


def move_fall():

    if random.random() < up_percent:
        agents[i][2] +=1
        
    elif random.random() > (up_percent) and random.random() < (up_percent + down_percent):
        agents[i][2] -=1
        
    else:
        agents[i][2] +=0
            

def move_nsew():

    
    if random.random() < north_percent:
        agents[i][0] -= 1
        
    elif random.random() > (north_percent) and random.random() < (north_percent + east_percent):
        agents[i][1] += 1

    elif random.random() > north_percent + east_percent and random.random() < (north_percent + east_percent + south_percent):
        agents[i][0] += 1
            
    else:    
        agents[i][1] -= 1
            
# Lets try and make it do both.

for i in range(number_particles):
    while (agents[i][2] > 0):    
        if agents[i][2] >= 75:
            move_fall()
            move_nsew()
        elif agents [i][2] < 75:
            agents[i][2] -= 1
            move_nsew()

# plot particles on map            
for i in range(number_particles):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])   
matplotlib.pyplot.show() 
   
print(agents)

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
import agentframework

#create empty lists
environment = []
agents = []


#create variables
buildingpos = 255
number_particles = 10

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
    agents.append(agentframework.Particle())


     
# Lets try and make it do both.

for i in range(number_particles):
    while (agents[i].z > 0):    
        if agents[i].z >= 75:
            agents[i].move_fall()
            agents[i].move_nsew()
        elif agents [i].z < 75:
            agents[i].z -= 1
            agents[i].move_nsew()

# plot particles on map            
for i in range(number_particles):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   
matplotlib.pyplot.show() 
   


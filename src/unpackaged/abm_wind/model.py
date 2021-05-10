# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:11:35 2021

@author: katie
"""

#bacteria bomb tracking particle model

#import nesc modules

import csv
import matplotlib.pyplot
#import random
import agentframework

#create empty lists
environment = []
agents = []


#create variables
buildingpos = 255
number_particles = 5000

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

#print(bombloc) # just to check there is a coordinate
bomb = (bombloc[0]) # since it was a tuple in the list
bomb_y = (bomb[0]) 
bomb_x = (bomb[1])


# Make the Agents

for i in range(number_particles):
    agents.append(agentframework.Particle(environment))

     
# Lets try and make it fall and move.

for i in range(number_particles):
    while (agents[i].z > 0):    
        if agents[i].z >= 75:
            agents[i].move_fall()
            agents[i].move_nsew()
        elif agents [i].z < 75:
            agents[i].z -= 1
            agents[i].move_nsew()

# try to mark in the environemnet where the particles have settled
for i in range(number_particles):
    agents[i].settle()
    

matplotlib.pyplot.imshow(environment)
#plot particles on map       
for i in range(number_particles):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   
matplotlib.pyplot.show() 
   
#Export CSV file with updated environement values

with open('fallout.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=' ')
    wr.writerows(environment)
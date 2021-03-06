# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:11:35 2021

@author: katie
"""

#bacteria bomb tracking particle model

#import nesc modules

import csv
import matplotlib
matplotlib.use('TkAgg') 
import tkinter
import matplotlib.pyplot
import agentframework


#create empty lists
environment = []
agents = []


#create variables
buildingpos = 255
number_particles = 5000
fig = matplotlib.pyplot.figure(figsize=(7, 7))
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
bomb_y = (bomb[0]) # y coordinate
bomb_x = (bomb[1]) # x coordinate

# Make the Agents

for i in range(number_particles):
    agents.append(agentframework.Particle(environment))

    
# Lets try and make it fall and move and create function to run the model
def run():
    """
    Runs the model

    Returns:
    None
    """  

    for i in range(number_particles):
        while (agents[i].z > 0):    #move while still in above groundlevel
            if agents[i].z >= 75:   #move up or down if over building height
                agents[i].move_fall()
                agents[i].move_nsew()
            elif agents [i].z < 75: #move down 1 when height below building height
                agents[i].z -= 1
                agents[i].move_nsew()
   
    
    matplotlib.pyplot.rc('image', cmap='OrRd')
    matplotlib.pyplot.imshow(environment)
#print(agents) #Check that they have moved and all at height 0 (ground level)
#plot particles on map     
       
    for i in range(number_particles):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)  
        
# Mark in the environment where the particles have settled
    for i in range(number_particles):
        agents[i].settle()
        
    canvas.draw()
 
#Export CSV file with updated environement values
def export_fallout():
    """
    Exports the fall out as a csv file

    Returns:
    None
    """  
    with open('fallout.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, delimiter=',')
        wr.writerows(environment)




#create GUI

root = tkinter.Tk()
root.wm_title("Bacteria Bomb!")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Bomb", menu=model_menu)
model_menu.add_command(label="Detonate", command=run)
model_menu.add_command(label="Export Data", command=export_fallout)

tkinter.mainloop()

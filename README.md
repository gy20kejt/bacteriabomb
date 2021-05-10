# Bacteria Bomb!

This project is for assignment 2 of Geog5003m at the University of Leeds.  
It is based on instructions, quoted and paraphrased below for tracking biological weapon fallout.

## Briefing
"Imagine someone lets off a biological weapon in the middle of a town on top of a building. The bacteria it releases is deadly on contact, and you, as a member of a secret government anti-terrorist unit want to trace where it goes so you can deal with the contamination. You need to build a model of the spread so you can estimate the location of the bacteria."

With information for the probability of particles being moved up and down and moving in the cardinal directions we were required to build a program to do the following...

    Pull in the data file and find the bomb location.

    Calculate where 5000 bacteria will end up.

    Draw a density map of where all the bacteria end up as an image and displays it on the screen.

    Save the density map to a file as text.

A basic algorithm is, for each particle, to move the particle up and along in a loop that picks randomly the way it will go. When it hits the ground, you make a note of where it hit by incrementing a 2D array by one, and start with the next particle. 

## Files

[Model](https://github.com/gy20kejt/bacteriabomb/blob/main/src/unpackaged/abm_wind/model.py) This is the main file that runs the program.

[Agent Framework](https://github.com/gy20kejt/bacteriabomb/blob/main/src/unpackaged/abm_wind/agentframework.py) This is the basis for the agent 

[Environment](https://github.com/gy20kejt/bacteriabomb/blob/main/src/unpackaged/abm_wind/wind.raster) This is a 300 x 300 pixel raster file containing the location of the bomb provided with the briefing 

### License

This model is licensed under the MIT License.

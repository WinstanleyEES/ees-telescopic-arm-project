#!/usr/bin/python

# importing the modules and classes
import pygame
from pygame.locals import *
from guibase import Gui
from guiobject import GuiObject

# create the gui object
ArmEnv = Gui(500,500,(250,250,250), "Telescopic Arm Gui", 30)

# create the arm object
ArmObj = GuiObject(20, 20, (0,0,0), 0, 0)

# update and render everything for the first time - this allows the settings to initialize before the first frame is run
ArmEnv.update()
ArmEnv.render([ArmObj])

# creating the main while loop
while True :
	# getting all the pygame events
	for event in pygame.event.get() :
		# checking if the event is to quit pygame - then quit the program
		if event.type == pygame.QUIT :
			ArmEnv.terminate()
	
	# all other code shinanigans goes here
		#...
			
	# update everything that needs updating
	ArmEnv.update()
	
	# render everything to the screen
	ArmEnv.render([ArmObj])
	
	# tick the fps
	ArmEnv.clock.tick(ArmEnv.fps)
	
# fail safe quit
ArmEnv.terminate()
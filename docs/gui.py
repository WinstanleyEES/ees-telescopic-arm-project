#!/usr/bin/python
# -*- coding: latin-1 -*-
# importing the modules and classes
import pygame
from pygame.locals import *
from guibase import Gui
from guiobject import GuiObject
from textconstruct import TextConstruct

pygame.init()

# create the gui object
ArmEnv = Gui(500,540,(250,250,250), "Telescopic Arm Gui", 30)

# create the arm object
MenuBar = GuiObject(500, 40, (230,230,230), 0, 0, "lower")
ArmObj = GuiObject(20, 20, (0,0,0), 0, 40, "none")

# create the text constructor
ArmText = TextConstruct("monospace", 15, (0,0,0))

# update and render everything for the first time - this allows the settings to initialize before the first frame is run
ArmEnv.update()
ArmEnv.render([ArmObj, MenuBar], [])

# Creating a static test text element that won't be recreated every frame
TestText = ArmText.draw_text_line(["Testing Rendering Text ", "Two"], [(0,0,0),(25,30,150)], "left", 0, 520)

# creating the main while loop
while True :

	# processing the pygame input
	ArmEnv.process_input()
	
	# updating the arm data for text display each frame
	ArmTextData = ArmText.draw_text_line(["Rendering ", "Text ", "To ", "The ", "Screen "], [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (210,40,70)], "left", 0, 10)
	
	# test string to show updating text every frame
	ArmFPSData = ArmText.draw_text_line(["fps counter: ", str(round(ArmEnv.clock.get_fps(),2))], [(0,0,0),(25,130,50)], "left", 320, 10) 
	
	# all other code shinanigans goes here
		#...
			
	# update everything that needs updating
	ArmEnv.update()
	
	# render everything to the screen
	ArmEnv.render([MenuBar, ArmObj], [ArmTextData,TestText,ArmFPSData])
	
	# tick the fps
	ArmEnv.clock.tick(ArmEnv.fps)
	
# fail safe quit
ArmEnv.terminate()
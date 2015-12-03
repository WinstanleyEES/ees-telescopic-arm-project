#!/usr/bin/python
# importing the modules and classes
import pygame
from pygame.locals import *
from guibase import Gui
from guiobject import GuiObject
from textconstruct import TextConstruct

# initializing pygame
pygame.init()

# create the gui object - loading the icon image from the icon directory
ArmIcon = pygame.image.load("icons\icon.png")
ArmEnv = Gui(500,540,(250,250,250), "Telescopic Arm Gui", 30, ArmIcon)

# create the arm object
MenuBar = GuiObject(500, 40, (230,230,230), 0, 0, "lower")
ArmObj = GuiObject(20, 20, (0,0,0), 0, 40, "none")

# create the text constructor
ArmText = TextConstruct("monospace", 15, (0,0,0))

# update and render everything for the first time - this allows the settings to initialize before the first frame is run
ArmEnv.update()
ArmEnv.render([ArmObj, MenuBar], [])

# Creating a static test text element that won't be recreated every frame
TestText = ArmText.draw_text_line(["Testing Rendering Text ", "Two"], [(0,0,0),(25,30,150)], "centre", 0, 520, 0,ArmEnv.screen)

# creating the main while loop
while True :

	# processing the pygame input
	ArmEnv.process_input()
	
	# updating the arm data for text display each frame
	ArmTextData = ArmText.draw_text_line(["Rendering ", "Text ", "To ", "The ", "Screen "], [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (210,40,70)], "left", 0, 10, 2)
	
	# test string to show updating text every frame
	ArmFPSData = ArmText.draw_text_line(["fps counter: ", "{:.2f}".format(round(ArmEnv.clock.get_fps(),2))], [(0,0,0),(25,130,50)], "right", 0, 10, 2, ArmEnv.screen) 
	
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
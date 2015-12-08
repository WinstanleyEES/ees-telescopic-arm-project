#!/usr/bin/python
# importing the modules and classes
import pygame
from pygame.locals import *
from guibase import *

# initializing pygame
pygame.init()

# create the gui object - loading the icon image from the icon directory
ArmIcon = pygame.image.load("icon.png")
ArmEnv = Gui(800,840,(236,238,240), "Telescopic Arm Gui", 30, ArmIcon)

# create the arm object
MenuBar = GuiObject(800, 40, (61,64,69), 0, 0, False, False, 0, True, (43,46,51), 2)
ArmObj = GuiObject(40, 40, (0,250,0), 0, 120, True, False, 0)
RadObj = GuiObject(40, 40, (42,70,120), 240, 760, False, True, 760)
ArmPul = GuiObject(6, 40, (0,0,0), 17, 160, True, False, 0)

# create the text constructor
ArmText = TextConstruct("consolas", 20, (0,0,0), True)

# update and render everything for the first time - this allows the settings to initialize before the first frame is run
ArmEnv.update()
ArmEnv.render([MenuBar, ArmObj], [])

# Creating a static test text element that won't be recreated every frame
TestText = ArmText.draw_text_line(["Testing Rendering Text ", "Two"], [(0,0,0),(25,30,150)], "centre", 0, 820, 0, ArmEnv.screen)

# creating the main while loop
while True :

	# processing the pygame input
	ArmEnv.process_input([ArmObj, ArmPul, RadObj])
	
	# updating the arm data for text display each frame
	ArmTextData = ArmText.draw_text_line(["Rendering ", "Text ", "To ", "The ", "Screen "], [(151,154,159), (151,154,159), (151,154,159), (151,154,159), (210,40,70)], "left", 0, 10, 5)
	
	# test string to show updating text every frame
	ArmFPSData = ArmText.draw_text_line(["fps counter: ", "{:.2f}".format(round(ArmEnv.clock.get_fps(),2))], [(151,154,159),(25,130,50)], "right", 0, 10, 5, ArmEnv.screen) 
	
	# all other code shinanigans goes here
		#...
	#RadObj.gravity()
			
	# update everything that needs updating
	ArmEnv.update()
	
	# render everything to the screen
	ArmEnv.render([MenuBar, ArmObj, RadObj, ArmPul], [ArmTextData,TestText,ArmFPSData])
	
	# tick the fps
	ArmEnv.clock.tick(ArmEnv.fps)
	
# fail safe quit
ArmEnv.terminate()
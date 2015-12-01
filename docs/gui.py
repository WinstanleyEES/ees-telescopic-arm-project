import pygame
from pygame.locals import *
from guibase import Gui
from guiobject import GuiObject

# create the gui object
ArmEnv = Gui(500,500,(250,250,250), "Telescopic Arm Gui", 30)

# create the arm object
ArmObj = GuiObject(20, 20, (0,250,0), 0, 0)

# initialize the pygame clock
clock = pygame.time.Clock()
ArmEnv.update()


while True :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			ArmEnv.terminate()
	
	# render everything
	ArmEnv.render([ArmObj])
	
	# tick the fps
	ArmEnv.clock.tick(ArmEnv.fps)
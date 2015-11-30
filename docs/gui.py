import pygame
from pygame.locals import *
from guiClass import Gui

ArmEnv = Gui(500,500,(250,250,250), "Telescopic Arm Gui", 30)
clock = pygame.time.Clock()

while True :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			ArmEnv.terminate()
		elif event.type == pygame.MOUSEBUTTONDOWN :
			print "Clicked"
	
	ArmEnv.render()
	
	clock.tick(ArmEnv.fps)
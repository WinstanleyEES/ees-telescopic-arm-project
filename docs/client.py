#!/usr/bin/python

import socket
import sys
import time
import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(17, GPIO.OUT) # Y
GPIO.setup(27, GPIO.OUT) # Z
GPIO.setup(22, GPIO.OUT) # T
GPIO.setup(10, GPIO.OUT) # Z
GPIO.setup(9, GPIO.OUT)  # Y
GPIO.setup(11, GPIO.OUT) # T

LIGHTONY = False
LIGHTONZ = False
LIGHTONT = False
MAGSTATE = False

HOST = "192.168.43.141"
PORT = 3443

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

while True :
	data = c.recv(1024)
	print data
	
	if len(data) > 0 :
		if data == "joystickpos" :
			print "[+] getting joystick data."
			while True :
				joyaxis = c.recv(1024)
				if joyaxis != "quit" :
					joydata = joyaxis.split(",")
					
					Y = float((joydata[0])[:5])
					Z = float((joydata[1])[:5])
					T = float((joydata[2])[:5])
					C = int((joydata[3])[:2])
					M = int((joydata[4])[:2])

					if Y <= -0.5 :
						print "Y += 1"
						GPIO.output(27, GPIO.HIGH)
						GPIO.output(10, GPIO.LOW)
						
					elif Y >= 0.5 :
						print "Y -= 1"
						GPIO.output(10, GPIO.HIGH)
						GPIO.output(27, GPIO.LOW)
						
					else :
						GPIO.output(27, GPIO.LOW)
						GPIO.output(10, GPIO.LOW)

					if Z <= -0.5 :
						print "Z += 1"
						GPIO.output(17, GPIO.HIGH)
						GPIO.output(9, GPIO.LOW)
						
					elif Z >= 0.5 :
						print "Z -= 1"
						GPIO.output(9, GPIO.HIGH)
						GPIO.output(17, GPIO.LOW)
						
					else :
						GPIO.output(17, GPIO.LOW)
						GPIO.output(9, GPIO.LOW)

					if T <= -0.5 and T >= -1.0 and MAGSTATE == False :
						print "Trigger Pressed"
						GPIO.output(22, GPIO.HIGH)
						GPIO.output(11, GPIO.LOW)
						MAGSTATE = True
						
					elif T <= -0.5 and T >= -1.0 and MAGSTATE == True :
						print "Trigger Unpressed"
						GPIO.output(22, GPIO.LOW)
						GPIO.output(11, GPIO.HIGH)
						MAGSTATE = False
					
				else :
					print("[+] No longer receiving joystick data.")
					GPIO.cleanup()
					break
					
		elif data == "quit" :
			print "[+] Quitting..."
			break
			
sys.exit()
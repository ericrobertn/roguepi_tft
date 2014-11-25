#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os

#Set GPIO mode
GPIO.setmode(GPIO.BCM)

#Setup GPIO
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Set up backlight GPIO
os.system("sudo sh -c 'echo 252 > /sys/class/gpio/export'")

#Give the system a quick break
time.sleep(0.5)

#Set the intitial counter value to zero
counter = 0

#var for the 'while' statement to keep it running
var = 1

#Main program
while var == 1:
 if (GPIO.input(23) == False): #Backlight control

  if (counter == 0):
   os.system("sudo sh -c 'echo 'out' > /sys/class/gpio/gpio252/direction'")
   counter = 1
   print("counter now 1")
   time.sleep(0.5)

  elif (counter == 1) or (counter == 3):
   os.system("sudo sh -c 'echo '1' > /sys/class/gpio/gpio252/value'")
   counter = 2
   print("counter now 2")
   time.sleep(0.5)

  elif (counter == 2):
   os.system("sudo sh -c 'echo '0' > /sys/class/gpio/gpio252/value'")
   counter = 3
   print("counter now 3")
   time.sleep(0.5)

 if (GPIO.input(22) == False):
  print("22 Working")
  time.sleep(0.5)

 if (GPIO.input(27) == False):
  os.system(kill)
  print("27 working")
  time.sleep(0.5)

 if (GPIO.input(18) == False):
  print("TEST")
  os.system("python /home/neo/documents/rogue_pi/ip_add")

GPIO.cleanup()

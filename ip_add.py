#! /usr/bin/env python

from pygame.locals import *
from subprocess import call
from time import sleep
from sys import exit
from ConfigParser import SafeConfigParser


import smbus
import subprocess
import re
import socket
import fcntl
import struct
import socket
import signal
import sys, pygame
import time
import os


os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

#define network interface
iface = 'eth0'
ham = 'ham0'

# Function which gets the Default IP address
def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
        )[20:24])


# def dhcp_check():
        # if int(ip_address = get_ip_address(iface)) > 0:
                # font=pygame.font.Font(None,24)
                # label=font.render("Failure", 1, (red))
                # screen.blit(label,(40,120))
                # pygame.display.flip()
                # #print packet_loss + " packet loss."
        # else:
                # font=pygame.font.Font(None,24)
                # label=font.render("Success", 1, (green))
                # screen.blit(label,(40,120))
                # pygame.display.flip()


# Function which gets the Default Gateway IP address
def get_gateway(ifname):
    proc = subprocess.Popen("ip route list dev " + ifname + " | awk ' /^default/ {print $3}'", \
    shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return_code = proc.wait()
    for line in proc.stdout:
        line
    return line

def make_stext(text, xpo, ypo, colour):
    font=pygame.font.Font(None,18)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

def make_text(text, xpo, ypo, colour):
    font=pygame.font.Font(None,24)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

def make_button(text, xpo, ypo, colour):
    font=pygame.font.Font(None,24)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

        #Ping Google Check
def ping_google():
        proc = subprocess.Popen("ping -c 2 google.com 2>&1", \
                        shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        return_code = proc.wait()

        # Read from pipes
        # stdout
        for line in proc.stdout:
                if "loss" in line:
                        packet_loss = progress = re.search('\d*%',line).group()
                        if int(packet_loss.split('%')[0]) > 0:
                                font=pygame.font.Font(None,24)
                                label=font.render("Failure", 1, (red))
                                screen.blit(label,(40,120))
                                pygame.display.flip()
                                #print packet_loss + " packet loss."
                        else:
                                font=pygame.font.Font(None,24)
                                label=font.render("Success", 1, (green))
                                screen.blit(label,(40,120))
                                pygame.display.flip()

        #Ping Gateway
def ping_gateway():
        ip_gateway = get_gateway(iface)

        proc = subprocess.Popen ("ping -c 2 " + ip_gateway + " 2>&1", \
                        shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        return_code = proc.wait()

        # Read from pipes
        # stdout
        for line in proc.stdout:
           if "loss" in line:
                   packet_loss = re.search('\d*%',line).group()
                   if int(packet_loss.split('%')[0]) > 0:
                                font=pygame.font.Font(None,24)
                                label=font.render("Failure")
                                screen.blit(label,(180,80))
                                pygame.display.flip()
                           #print ip_gateway + packet_loss + " packet loss for gateway."
                   else:
                        font=pygame.font.Font(None,24)
                        label=font.render("Success", 1, (green))
                        screen.blit(label,(180,80))
                        pygame.display.flip()
                           #print "Gateway is reachable"


#Get Number of hosts from Nmap scan run at ./installer.sh
def number_hosts():
    proc = subprocess.Popen("cat /pentest/dumps/nmap-testinit | grep -o -P '.{0,20}hosts.{0,20}'", \
        shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return_code = proc.wait()
    for line in proc.stdout:
        line
    return line





#set size of screen
size = width, height = 320, 240

#define colours
blue = 26, 0, 255
cream = 254, 255, 250
black = 0, 0, 0
white = 255, 255, 255
green = 127, 255, 0
red = 255,0 ,0

screen = pygame.display.set_mode(size)

#welcome screen
screen.fill(black)
font=pygame.font.Font(None,36)
label=font.render("Rogue Pi_", 1, (red))
screen.blit(label,(60,80))
pygame.display.flip()
time.sleep(5)
pygame.display.update()

screen.fill(black)
font=pygame.font.Font(None,36)
label=font.render("Loading Network Info...", 1, (white))
screen.blit(label,(20,80))
pygame.display.flip()
time.sleep(1)
pygame.display.update()

screen.fill(black)

#This is where the text goes
make_button("IP Address:", 20, 20, white)
make_text(get_ip_address(iface),40,40,green)

make_button("Defualt Gateway:     Pinging Gateway",20,60,white)
make_text(get_gateway(iface),40,80,green)
print ping_gateway()


make_button("Pinging Google",20, 100,white)
print ping_google()

make_button("Secure Tunnel",20, 140,white)
make_text(get_ip_address(ham),40,160,green)

make_button("Number of Hosts on Network:", 20, 180, white)
make_stext(number_hosts(),20,210,blue)

make_text("RoguePi_",200,10,red)
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "screen pressed" #for debugging purposes
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            print pos #for checking
            pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
            on_click()

#ensure safe exit

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()


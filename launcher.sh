#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
# add this as a cron job to launch on boot



cd /
cd root/Documents/rogue_pi
sudo python buttons.py
cd /

roguepi_tft
===========

Put on hold due to 
>  File "buttons.py", line 79, in <module>
    screen = pygame.display.set_mode((640, 480))
pygame.error: Unable to open mouse



This is a set of python files to to use an Adafruit PiTFT - 2.8" Touchscreen Display for Raspberry Pi to create a pen testing drop box

http://imgur.com/VuqNL80

I've created a python script that will fill a sceen with 

IP Address

Default Gateway (Success / Failure Ping)

Pinging Google (Success / Failure)

Secure Tunnel Conenction # Using log-me-in hamachi at the moment but may switch to home SSH/VPN tunnel

Number of Hosts on network #In the works (Nmap on boot output host number to file?)


#I want to add a Python script on boot to enable PiTFT buttons to do the following
Added script launcer.sh to cd into directory and launch buttons.py

Screen on/off?

Power pi on/off?


Also have touch screen capabilities. Hopefully can create a menu to choose pentesting tools and launch via on screen menu and buttons.



Moving forward: 

Things to add..

• Better looking tsatus Report of the Rogue Pi: IP, Tunnel Up or Down, Gateway, Internet Connectiviy,

• nmap portscan (you’d need to a script which could gather a bit of info about the network and pass that info into the nmap arguments but shouldn’t be hard.) Have the screen show a progress bar so you can determine how long that scan is going to take and then dump the contents into a file and print the location on the screen

• Enable / Disable Wireless Adapter

• Airmon-ng: Assuming you have a network adapter perform a quick scan of the airwaves and print out a scrollable list of nearby APs (SSID, single strength, encryption Type, BSSID)

• Tunneling Options

• Self-destruct mode



I've had this idea for awhile but the code from the Rogue Pi project helped get me started.

http://crushbeercrushcode.org/2013/03/developing-the-rogue-pi/

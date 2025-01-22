# Installing Raspberry Pi OS without any external monitor or keyboard

## Flashing the Raspberry Pi OS on your microSD Card

* Go to https://www.raspberrypi.com/software/
* Download Raspberry Pi images for macOS, Windows, or Linux
* Install it and launch it
* Select options: 
  * Device: Raspberry Pi 4
  * OS: Raspberry Pi OS (64-bit)
  * Storage: microSD card
* Before doing anything, make sure you're on the same WiFi network you will use for your raspberry pi
* Edit settings
  * Set hostname to "raspberrypi2"
  * Set username to "pi"
  * Set password to whatever you want
  * Enter WiFi info
* Save and install

## Boot your Raspberry Pi for the first time

* Plug it in.

## Find the Raspberry Pi's IP address

* I used the Unifi router for this.

## Connect to your Pi using SSH

* Open the terminal of choice
* ssh pi@raspberrypi2.local or the raspberrypi2 IP address

## Set up VNC to get remote access to your Raspberry Pi OS Desktop 

* SSH into the Raspberry Pi
* `sudo raspi-config`
*  Interface Options
  * Enable VNC Server
* System Options
  * Boot / Auto Login
    * Desktop Autologin
* Finish and reboot
* Then log in with your VNC client. I'm using "TigerVNC" (1.14.1) on my Mac.
  * Sometimes Home IP addresses change, so you may need to find the IP address again.

## Finish the Startup Configuration

TODO

## Extra: Raspberry Pi Connect

TODO

## Extra: If you have to connect to a new WiFi network

TODO

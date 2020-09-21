# UPS-Display
Python3 script to show info about APC UPSes (via apcupsd-refresh every 10 seconds) on a Waveshare e-ink display and a RPi Zero W. 
The display used is the "Waveshare 2.13inch e-Paper HAT", you can read more at this link: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
We will take the data from https://github.com/flyte/apcaccess

Tested with a APC Back-UPS XS 700U and a Pi Zero W Rev1.1

![GitHub Logo](/images/poc.jpg)

_______________________________________________________________________________________________

Before you start, make sure you have the SPI interface enabled on your Raspberry

	sudo raspi-config
	Choose Interfacing Options > SPI > Yes  to enable SPI interface
	sudo reboot
_______________________________________________________________________________________________

We need to get the required packages and libraries on the RPi Zero W:

Install the required packages to build BCM libraries:

	sudo apt-get install gcc make libc-dev 

Download and install BCM2835 libraries:

	wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
	tar zxvf bcm2835-1.60.tar.gz 
	cd bcm2835-1.60/
	sudo ./configure
	sudo make
	sudo make install

Install python3 and the required libraries and modules:

	apt-get install python3 python3-pip python3-pil python3-numpy python3-rpi.gpio python3-smbus wiringpi
	python3 -m pip install spidev
	python3 -m pip install RPi.GPIO
	python3 -m pip install setuptools
	python3 -m pip install apcaccess
	
Now you can clone this repository, open the file upsdisplay.py and modify "YOUR_RASPI_IP" with the IP address of your Raspberry Pi.
To run the script in background execute: 

	python3 upsdisplay.py&

_______________________________________________________________________________________________
Note: 
This project has been realized for personal use. 
I am not a developer, it is the first application I write in Python and it may not be optimized or formally correct. 

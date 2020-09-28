# UPS-Display
Python3 script to show info about APC UPSes on a e-Paper display and a RPi Zero W. 

![GitHub Logo](/images/poc.jpg)


# What you need
* [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) with [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) installed (former name was Raspbian)
* [Waveshare e-Paper 2.13inch Display](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT)

Before you start, make sure you have the SPI interface enabled on your Raspberry

	sudo raspi-config
	Choose Interfacing Options > SPI > Yes  to enable SPI interface
	sudo reboot

# Displayed info:
- Status
- Load
- Charge
- Time left
- Voltage
- Firmware
- Serial
- Model  

# Setup:
1) Install the required packages to build BCM libraries:

		sudo apt-get install gcc make libc-dev 

2) Download and install BCM2835 libraries:

		wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
		tar zxvf bcm2835-1.60.tar.gz 
		cd bcm2835-1.60/
		sudo ./configure
		sudo make
		sudo make install

3) Install python3 and the required libraries and modules:

		apt-get install python3 python3-pip python3-pil python3-numpy python3-rpi.gpio python3-smbus wiringpi
		python3 -m pip install spidev
		python3 -m pip install RPi.GPIO
		python3 -m pip install setuptools
		python3 -m pip install apcaccess
	
4) Now you can clone this repository, open the file upsdisplay.py and modify "YOUR_RASPI_IP" with the IP address of your Raspberry Pi.
5) To run the script in background execute: 

		python3 upsdisplay.py&
	
# Acknowledgements:

* [Apcaccess python library](https://github.com/flyte/apcaccess)
* [e-paper Display library](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT)
* Tested with an [APC Back-UPS XS 700U](https://www.apc.com/shop/my/en/products/APC-Back-UPS-700VA-230V-AVR-Universal-and-IEC-Sockets/P-BX700U-MS) and a Pi Zero W Rev1.1

# Notes: 
This project has been realized for personal use. 
I am not a developer, it is the first application I write in Python and it may not be optimized or formally correct. 

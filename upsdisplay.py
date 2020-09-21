#!/usr/bin/python
#
#Author: Stinocon
#Date: 21 Sep 2020
#
import sys
import os
import time
import logging
sys.path.insert(1, "./lib")
sys.path.insert(1, "./pic")
from lib import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont
from apcaccess import status as apc
#logging.basicConfig(level=logging.DEBUG)

while True:
 apcdata = apc.parse(apc.get(host="YOUR_RASPI_IP"), strip_units=True)
 status = apcdata["STATUS"]
 load = apcdata["LOADPCT"]
 charge = apcdata["BCHARGE"]
 timeleft = apcdata["TIMELEFT"]
 try:
     epd = epd2in13_V2.EPD()
     epd.init(epd.FULL_UPDATE)
     # Drawing on the image
     font15 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 15)
     font24 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 24)
     image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
     draw = ImageDraw.Draw(image)
     #logging.info("epd2in13_V2 print test")
     draw.text((57, 0), 'UPS Status', font = font24, fill = 0)
     draw.text((0, 35), 'Status:' + status, font = font15, fill = 0)
     draw.text((0, 55), 'Load:' + load, font = font15, fill = 0)
     draw.text((0, 75), 'Charge:' + charge, font = font15, fill = 0)
     draw.text((0, 95), 'Time left:' + timeleft, font = font15, fill = 0)
     epd.display(epd.getbuffer(image))
     time.sleep(10)
 except IOError as e:
     logging.info(e)
 except KeyboardInterrupt:
     epd2in13_V2.epdconfig.module_exit()

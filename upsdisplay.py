#!/usr/bin/python
#
#Author: Stinocon
#Date: 23 Sep 2020
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
 voltage = apcdata["LINEV"]
 firmware = apcdata["FIRMWARE"]
 serial = apcdata["SERIALNO"]
 model =  apcdata["MODEL"]
 #print (apcdata) #uncomment to print info about your UPS via cli
 try:
     epd = epd2in13_V2.EPD()
     epd.init(epd.FULL_UPDATE)
     font15 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 15)
     font24 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 24)
     image = Image.new('1', (epd.height, epd.width), 255)
     draw = ImageDraw.Draw(image)
     #logging.info("epd2in13_V2 print test")
     draw.text((57, 0), 'UPS Status', font = font24, fill = 0)
     draw.text((0, 35), 'Status:' + status, font = font15, fill = 0)
     draw.text((0, 55), 'Load:' + load, font = font15, fill = 0)
     draw.text((0, 75), 'Charge:' + charge, font = font15, fill = 0)
     draw.text((0, 95), 'Time left:' + timeleft, font = font15, fill = 0)
     epd.display(epd.getbuffer(image))
     time.sleep(5)
     epd.init(epd.FULL_UPDATE)
     font15 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 15)
     font24 = ImageFont.truetype('/opt/ups-display/pic/Font.ttc', 24)
     image = Image.new('1', (epd.height, epd.width), 255)
     draw = ImageDraw.Draw(image)
     draw.text((57, 0), 'UPS Status', font = font24, fill = 0)
     draw.text((0, 35), 'Voltage:' + voltage, font = font15, fill = 0)
     draw.text((0, 55), 'Firmware:' + firmware, font = font15, fill = 0)
     draw.text((0, 75), 'S/N:' + serial, font = font15, fill = 0)
     draw.text((0, 95), 'Model:' + model, font = font15, fill = 0)
     epd.display(epd.getbuffer(image))
     time.sleep(5)
 except IOError as e:
     logging.info(e)
 except KeyboardInterrupt:
     epd2in13_V2.epdconfig.module_exit()

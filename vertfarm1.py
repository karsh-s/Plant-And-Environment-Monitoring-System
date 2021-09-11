#!/usr/local/bin/python
#  Importing all modules needed for the sensors
import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import csv
from PiAnalog import*
from datetime import datetime
import Adafruit_MCP3008
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from statistics import mean
from subprocess import call

#  Setting up variables for the date, the GPIO channel and the pi readings
p = PiAnalog()
datetime_object=datetime.now()
channel =21
am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

#  Setting up all GPIO modes and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setwarnings(False)
Moisture=GPIO.input(channel)

#Taking photo and finding the height of the plant
def capture(counter):
    filename="day" + str(counter) + ".jpg"
    call(["fswebcam","-d","/dev/video0","-r","1920x1080","--no-banner","/home/pi/DiptoSessions/STSVerticalFarm/static/source_images/"+filename])

#  Opening CSV file to be abl to write on 
f = open("static/demofile3.csv", "a")

dhtDevice = adafruit_dht.DHT11(board.D4)

#  Starts a loop
for i in range(1000):
     try:
    # Finds the sensor data and if needed, converts to percent
      temperature_c = dhtDevice.temperature
      humidity = dhtDevice.humidity
      datetime_object=datetime.now()
      moisture_value = am.read_adc(0)
      per = moisture_value * 100 / 1023
      dt = datetime_object.strftime('%Y%m%d%H%M%S')
      capture(dt)
    
    # Prints all data in terminal
      print(datetime_object)
      print(temperature_c)
      print(humidity)
      print(p.read_resistance())
      print(per)
      
    # Writes data into CSV file
      f.write(str(datetime_object))
      f.write(",%-3.1f" % temperature_c)
      f.write(",%-3.1f" % humidity)
      f.write(",%-3.1f" % p.read_resistance())
      f.write(",%-3.1f\n" % per)
      
    
    # When there is an error, print error and wait 30seconds before trying again
     except RuntimeError as error:
      print(error.args[0])
      time.sleep(30.0)
      continue
    
    # When there is no error, repeat the sequence every 30 seconds
     except Exception as error:
      dhtDevice.exit()
      raise error
     time.sleep(3.0)

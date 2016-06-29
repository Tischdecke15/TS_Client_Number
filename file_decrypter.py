#!/usr/bin/python
import subprocess, time, RPi.GPIO as GPIO

GPIO.setwarnings(False)

SDI   = 13
RCLK  = 19
SRCLK = 26
segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):
	for bit in range(0, 8):
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

def displayNumber(numberx):
	hc595_shift(segCode[numberx])

subprocess.call("./ServerQueryDataProcessing.sh", shell=True)
file = open("file.txt", "r+")
file.seek(12, 0)
str = file.read()
file.close

fileparts = str.split('|')
del fileparts[-1]
for i in range(len(fileparts)):
    print(fileparts[i])

setup()
displayNumber(len(fileparts))


exit()

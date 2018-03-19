# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
	exit()

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
SERVO1 = 13
SERVO2 = 19

MIN_HEIGHT = 800
MAX_HEIGHT = 2300
MIN_WIDTH = 900
MAX_WIDTH = 2200
width = 1400
height = 1500

step = 100

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(IN1,GPIO.OUT)
	GPIO.setup(IN2,GPIO.OUT)
	GPIO.setup(IN3,GPIO.OUT)
	GPIO.setup(IN4,GPIO.OUT)
	GPIO.setup(SERVO1,GPIO.OUT)
	GPIO.setup(SERVO2,GPIO.OUT)

def forward():
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)

def back():
	GPIO.output(IN1,GPIO.LOW)
	GPIO.output(IN2,GPIO.HIGH)
	GPIO.output(IN3,GPIO.LOW)
	GPIO.output(IN4,GPIO.HIGH)

def left():
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)

def right():
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)

def stop():
	GPIO.output(IN1,GPIO.LOW)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,GPIO.LOW)
	GPIO.output(IN4,GPIO.LOW)

def s_down():
	global height
	print(height)
	if height+step<MAX_WIDTH:
		height +=step
		pi.set_servo_pulsewidth(SERVO1,height)
		time.sleep(0.1)
	else:
		height = MAX_WIDTH

def s_up():
	global height
	print(height)
	if height-step>MIN_WIDTH:
		height -=step
		pi.set_servo_pulsewidth(SERVO1,height)
		time.sleep(0.1)
	else:
		height = MIN_HEIGHT
	print(height)

def s_left():
	global width
	print(width)
	if width+step<MAX_WIDTH:
		width +=step
		pi.set_servo_pulsewidth(SERVO2,width)
		time.sleep(0.1)
	else:
		width = MAX_HEIGHT
	print(width)

def s_right():
	global width
	print(width)
	if width-step>MIN_WIDTH:
		width -=step
		pi.set_servo_pulsewidth(SERVO2,width)
		time.sleep(0.1)
	else:
		width = MIN_WIDTH
	print(width)

def s_center():
	global height
	global width
	width = 1400
	height = 1500
	pi.set_servo_pulsewidth(SERVO2,width)
	time.sleep(0.1)
	pi.set_servo_pulsewidth(SERVO1,height)
	time.sleep(0.1)

def cleanup():
	GPIO.cleanup()
#init()

#forward()
#back()
#left()
#right()
#GPIO.cleanup()


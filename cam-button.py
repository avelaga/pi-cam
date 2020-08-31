from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
buttonPin = 18
GPIO.setup(buttonPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)

camera = PiCamera()
#camera.resolution = (2592,1944)
count = 0

while True:
	if GPIO.input(buttonPin) == 0:
		camera.start_preview()
		sleep(1)
		camera.capture('/home/pi/cam/button/button-%s.jpg' % count)
		camera.stop_preview()
		count+=1


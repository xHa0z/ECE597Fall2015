import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from Adafruit_LED_Backpack import BicolorMatrix8x8

display = BicolorMatrix8x8.BicolorMatrix8x8()

display.begin()
display.clear()
display.write_display()

BTN2 = "P9_11"
BTN1 = "P9_15"
BTN3 = "P9_21"
BTN4 = "P9_27"
BTN5 = "P9_12"


LED2 = "P9_13"
LED1 = "P9_17"
LED3 = "P9_23"
LED4 = "P9_29"


GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.add_event_detect(BTN1, GPIO.RISING)
GPIO.add_event_detect(BTN2, GPIO.RISING)
GPIO.add_event_detect(BTN3, GPIO.RISING)
GPIO.add_event_detect(BTN4, GPIO.RISING)
GPIO.add_event_detect(BTN5, GPIO.RISING)


size = 8
currentX = 0
currentY = 0
playground = []
for i in range(0,size):
	temp=[]
	for j in range(0,size):
		temp.append(0)
	playground.append(temp)

#playground[currentX][currentY] = 1
display.set_pixel(currentX, currentY, 1)
display.write_display()

while(True):
	if GPIO.event_detected(BTN1):
		if currentX > 0:
			GPIO.output(LED1, not GPIO.input(LED1))
			currentX = currentX -1
			#playground[currentX][currentY] = 1
			display.set_pixel(currentX, currentY, 1)
			display.write_display()
		#	sleep(0.3)
	if GPIO.event_detected(BTN2):
		if currentX < 7:
			GPIO.output(LED2, not GPIO.input(LED2))
			currentX = currentX + 1
			#playground[currentX][currentY] = 1
			display.set_pixel(currentX, currentY, 1)
			display.write_display()
		#	sleep(0.3)
	if GPIO.event_detected(BTN3):
		if currentY > 0:
			GPIO.output(LED3, not GPIO.input(LED3))
			currentY = currentY -1
			#playground[currentX][currentY] = 1
			display.set_pixel(currentX, currentY, 1)
			display.write_display()
		#	sleep(0.3)
	if GPIO.event_detected(BTN4):
		if currentY < 7:
			GPIO.output(LED4, not GPIO.input(LED4))
			currentY = currentY +1
			#playground[currentX][currentY] = 1
			display.set_pixel(currentX, currentY, 1)
			display.write_display()
		#	sleep(0.3)

	if GPIO.event_detected(BTN5):
		display.clear()
		display.write_display()

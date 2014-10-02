import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from Adafruit_LED_Backpack import BicolorMatrix8x8
from eqep import eQEP

encoder1 = eQEP("/sys/devices/ocp.3/48302000.epwmss/48302180.eqep", eQEP.MODE_ABSOLUTE)


encoder2 = eQEP("/sys/devices/ocp.3/48304000.epwmss/48304180.eqep", eQEP.MODE_ABSOLUTE)


display = BicolorMatrix8x8.BicolorMatrix8x8()

display.begin()
display.clear()
display.write_display()


#set up encoder
encoder1.set_period(1000000000);
encoder2.set_period(1000000000);





"""
BTN2 = "P9_11"
BTN1 = "P9_15"
BTN3 = "P9_21"
BTN4 = "P9_27"
"""

BTN5 = "P9_12"


"""
LED2 = "P9_13"
LED1 = "P9_17"
LED3 = "P9_23"
LED4 = "P9_29"
"""

"""
GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
GPIO.setup(BTN5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


"""
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.add_event_detect(BTN1, GPIO.RISING)
GPIO.add_event_detect(BTN2, GPIO.RISING)
GPIO.add_event_detect(BTN3, GPIO.RISING)
GPIO.add_event_detect(BTN4, GPIO.RISING)
"""
GPIO.add_event_detect(BTN5, GPIO.RISING)


size = 8
currentX = 0
currentY = 0
oldData1 = 0
oldData2 = 0

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
	position1 = encoder1.get_position();
	position2 = encoder2.get_position();

	if(position1 < oldData1):
		if currentX > 0 :
#		print "pos1" + position1
			currentX = currentX - 1
			oldData1 = position1
			display.set_pixel(currentX,currentY,1)
			display.write_display()
			sleep(0.3)	
	if(position1 > oldData1):
		if currentX < 7 :
			currentX = currentX + 1
			oldData1 = position1
			display.set_pixel(currentX,currentY,1)
			display.write_display()
			sleep(0.3)
	if(position2 > oldData2):
		if currentY > 0 :
#		print "pos2" + position2
			currentY = currentY -1 
			oldData2 = position2
			display.set_pixel(currentX,currentY,1)
			display.write_display()
			sleep(0.3)
	if(position2 < oldData2):
		if currentY < 7 :
			currentY = currentY + 1
			oldData2 = position2
			display.set_pixel(currentX, currentY,1)
			display.write_display()
			sleep(0.3)
	if GPIO.event_detected(BTN5):
		display.clear()
		display.write_display()






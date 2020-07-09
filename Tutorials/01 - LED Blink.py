# Items needed: RaspberryPi, Breadboard, 2x Jumper cables, LED, 1kOhm Resistor
# Physical wiring should be as follows: 
#  GPIO 18 (Pin12) -> LED -> 1kOhm Resistor -> Ground (Pin6)

import RPi.GPIO as GPIO
import time

#Sets the GPIO moade as broadcom (matches the pinout linked in the README)
GPIO.setmode(GPIO.BCM)

#Sets up pin 18 as an output
GPIO.setup(18, GPIO.OUT)

for i in range(10):
    GPIO.output(18, True)
    time.sleep(2)
    GPIO.output(18, False)
    time.sleep(2)
    
GPIO.cleanup()
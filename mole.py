import RPI.GPIO as GPIO
import random
import time

def nextMole():
    pin = random.choice([12, 16, 20, 21])
    GPIO.output(pin, GPIO.HIGH)
    return pin

def detectHit(pin):
    in_12 = GPIO.input(12)
    in_13 = GPIO.input(13)
    in_19 = GPIO.input(19)
    in_26 = GPIO.input(26)
    
    if(pin == 6 and in_12):
        score += 1
        return True
    if(pin == 16 and in_13):
        score += 1 
        return True
    if(pin == 20 and in_19):
        score += 1
        return True
    if(pin == 21 and in_26):
        score += 1
        return True
    if(in_12 or in_13 or in_19 or in_26):
        return True
    return False


# Function to turn the lights off
def allOff():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    return

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO pins for lights
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
# GPIO pins for switches
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

start = time.time()
end = time.time()
time_lapsed = 0
score = 0
while (time_lapsed < 300):
    x = 0
    pin = nextMole()
    while(x<20):
        if(detectHit(pin)):
            break
        time.sleep(.1)
    allOff()
    time_lapsed = end - start
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# data orange 18
# clock green 23
# latch brown 24

DATA = 18
CLOCK = 23
LATCH = 24

GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)

GPIO.output(LATCH, 0) #we close the latch
GPIO.output(CLOCK, 0) #idk/


def pulseClock():
    GPIO.output(CLOCK, 1)
    time.sleep(.01)
    GPIO.output(CLOCK, 0)

def serLatch():
    GPIO.output(LATCH, 1)
    time.sleep(.01)
    GPIO.output(LATCH, 0)

#most significant bit out first!

def ssrWrite(value):
    for x in range(0, 8):
        temp = value & 0x80 #we turn the base 10 value into an 8 bit digit
        if temp == 0x80:
            GPIO.output(DATA, 1) #write HIGH
        else:
            GPIO.output(DATA, 0) #write LOW
        pulseClock()
        value = value << 0x01 #shift left
    serLatch()

def toBinary(value):
    binaryValue = '0b'
    for x in range(0, 8):
        temp = value & 0x80
        if temp == 0x80:
            binaryValue = binaryValue + '1'
        else:
            binaryValue = binaryValue + '0'
        value = value << 1
    return binaryValue

def main():
    try:
        #ssrWrite(16)
        if True:
            temp = 1
            for j in range(0, 16):
                ssrWrite(temp)
                temp = temp << 1
                time.sleep(.2)
    
            for j in range(0, 16):
                temp = temp >> 1
                ssrWrite(temp)
                time.sleep(.2)

        GPIO.cleanup()

    except KeyboardInterrupt:
        print "exiting"
        GPIO.cleanup()
    sys.exit(0)

main()



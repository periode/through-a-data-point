import sys
import RPi.GPIO as GPIO
import time

# NOTES
# each motor has a number 0-6
# each entry in the dictionary for each motor has a value for CLOCK, DATA and LATCH
# TODO need to determine values for going up and going down

GPIO.setmode(GPIO.BCM)
## 1
# data green 23
# clock blue 18
# latch orange 24

CLOCK_1 = 18
DATA_1 = 23
LATCH_1 = 24

## 2
# clock orange 6
# data purple 25
# latch yellow 32

CLOCK_2 = 6
DATA_2 = 25
LATCH_2 = 12

## 3
# clock white 6
# data grey 16
# latch white 20
CLOCK_3 = 26
DATA_3 = 16
LATCH_3 = 20

#PROBLEM when one motor is going in a group, it overwrites the current direction of the neighboring motor

motors = {
        "A": {
            "NEIGHBOUR": "B",
            "CLOCK": CLOCK_1, 
            "LATCH": LATCH_1, 
            "DATA": DATA_1,
            "DOWN": 3,
            "UP": 12,
            "STILL": 0,
            "CURRENT": "STILL"
            },
        "B": {
            "NEIGHBOUR": "A",
            "CLOCK": CLOCK_1, 
            "LATCH": LATCH_1, 
            "DATA": DATA_1,
            "DOWN": 48,
            "UP": 192,
            "STILL": 0,
            "CURRENT": "STILL"
            },
        "C": {
            "NEIGHBOUR": "D",
            "CLOCK": CLOCK_2, 
            "LATCH": LATCH_2, 
            "DATA": DATA_2,
            "DOWN": 3,
            "UP": 12,
            "STILL": 0,
            "CURRENT": "STILL"
            },
        "D": {
            "NEIGHBOUR": "C",
            "CLOCK": CLOCK_2, 
            "LATCH": LATCH_2, 
            "DATA": DATA_2,
            "DOWN": 48,
            "UP": 192,
            "STILL": 0,
            "CURRENT": "STILL"
            },
        "E": {
            "NEIGHBOUR": "F",
            "CLOCK": CLOCK_3, 
            "LATCH": LATCH_3, 
            "DATA": DATA_3,
            "DOWN": 3,
            "UP": 12,
            "STILL": 0,
            "CURRENT": "STILL"
            },
        "F": {
            "NEIGHBOUR": "E",
            "CLOCK": CLOCK_3, 
            "LATCH": LATCH_3, 
            "DATA": DATA_3,
            "DOWN": 48,
            "UP": 192,
            "STILL": 0,
            "CURRENT": "STILL"
            }
        }

GPIO.setup(CLOCK_1, GPIO.OUT)
GPIO.setup(DATA_1, GPIO.OUT)
GPIO.setup(LATCH_1, GPIO.OUT)

GPIO.setup(CLOCK_2, GPIO.OUT)
GPIO.setup(DATA_2, GPIO.OUT)
GPIO.setup(LATCH_2, GPIO.OUT)

GPIO.setup(CLOCK_3, GPIO.OUT)
GPIO.setup(DATA_3, GPIO.OUT)
GPIO.setup(LATCH_3, GPIO.OUT)

GPIO.output(LATCH_1, 0) #we close the latch
GPIO.output(LATCH_2, 0)
GPIO.output(LATCH_3, 0)
GPIO.output(CLOCK_1, 0) #idk/
GPIO.output(CLOCK_2, 0)
GPIO.output(CLOCK_3, 0)


def pulseClock(_id):
    GPIO.output(motors[_id]['CLOCK'], 1)
    #GPIO.output(CLOCK_1, 1)
    time.sleep(.01)
    GPIO.output(motors[_id]['CLOCK'], 0)
    #GPIO.output(CLOCK_1, 0)

def serLatch(_id):
    GPIO.output(motors[_id]['LATCH'], 1)
    #GPIO.output(LATCH_1, 1)
    time.sleep(.01)
    GPIO.output(motors[_id]['LATCH'], 0)
    #GPIO.output(LATCH_1, 0)

#most significant bit out first!
def ssrWrite(_id, _dir):
    motors[_id]["CURRENT"] = _dir
    neighbour = motors[_id]["NEIGHBOUR"]
    value = motors[_id][_dir] + motors[neighbour][motors[neighbour]["CURRENT"]]
    for x in range(0, 8):
        temp = value & 0x80 #we turn the base 10 value into an 8 bit digit
        if temp == 0x80:
             GPIO.output(motors[_id]['DATA'], 1) #write HIGH
             #GPIO.output(DATA_1, 1)
        else:
            GPIO.output(motors[_id]['DATA'], 0) #write LOW
            #GPIO.output(DATA_1, 0)
        pulseClock(_id)
        value = value << 0x01 #shift left
    serLatch(_id)

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

def reset():
    for key in motors:
        ssrWrite(key, "STILL")

def main():
    try:
        reset()
        #for key in motors:
        #    ssrWrite(key, "DOWN")
        GPIO.cleanup()

    except KeyboardInterrupt:
        print "exiting"
        GPIO.cleanup()
    sys.exit(0)

main()



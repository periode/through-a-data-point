import sys
import RPi.GPIO as GPIO
import time
import threading

# NOTES
# threading time

GPIO.setmode(GPIO.BCM)
## 1
CLOCK_1 = 18 #green
DATA_1 = 23 #blue
LATCH_1 = 24 #orange

CLOCK_2 = 6 #orange
DATA_2 = 25 #purple
LATCH_2 = 12 #yellow

CLOCK_3 = 26 #white
DATA_3 = 16 #grey
LATCH_3 = 20 #white

forward_first = [
    10, # 1010,
    6,  # 0110,
    5,  # 0101,
    9   # 1001
]
forward_second = [160, 96, 80, 144]

backward_first = [
    9, # 1001,
    5, # 0101,
    6, # 0110,
    10 # 1010
]
backward_second = [144, 80, 96, 160]

class Motor:
    def __init__(self, _id, _neighbour, _clock, _latch, _data):
        self.id = _id
        self.neighbour = _neighbour
        self.clock_pin = _clock
        self.latch_pin = _latch
        self.data_pin = _data
        if _id == "A" or _id == "C" or _id == "E":
            self.first = True
        else:
            self.first = False

        if(self.first):
            self.fwd = [10, 6, 5, 9]
            self.bwd = [9, 5, 6, 10]
        else:
            self.fwd = [160, 96, 80, 144]
            self.bwd = [144, 80, 96, 160]

    def clock(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.clock_pin, 1)
        time.sleep(.0001)
        GPIO.output(self.clock_pin, 0)

    def latch(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.latch_pin, 1)
        time.sleep(.0001)
        GPIO.output(self.latch_pin, 0)

    def writePin(self, value):
        for x in range(0, 8):
            temp = value & 0x80
            if temp == 0x80:
                GPIO.output(self.data_pin, 1)
            else:
                GPIO.output(self.data_pin, 0)
            self.clock()
            value = value << 0x01
        self.latch()

    def up(self, delay, steps):
        GPIO.setmode(GPIO.BCM)
        for i in range(0, steps):
            self.writePin(self.fwd[0])
            time.sleep(delay)
            self.writePin(self.fwd[1])
            time.sleep(delay)
            self.writePin(self.fwd[2])
            time.sleep(delay)
            self.writePin(self.fwd[3])
            
        self.reset()

    def down(self, delay, steps):
        for i in range(0, steps):
            self.writePin(self.bwd[0])
            time.sleep(delay)
            self.writePin(self.bwd[1])
            time.sleep(delay)
            self.writePin(self.bwd[2])
            time.sleep(delay)
            self.writePin(self.bwd[3])
        self.reset()

    def move(self, dir, delay, step):
        if dir == "up":
            t = threading.Thread(target=self.up, args=(delay, step))
            t.start()
        else:
            t = threading.Thread(target=self.down, args=(delay, step))
            t.start()

    def reset(self):
        for state in [0, 0, 0, 0]:
            self.writePin(state)

motors = []

motors.append(Motor("A", "B", CLOCK_1, LATCH_1, DATA_1))
motors.append(Motor("B", "A", CLOCK_1, LATCH_1, DATA_1))
motors.append(Motor("C", "D", CLOCK_2, LATCH_2, DATA_2))
motors.append(Motor("D", "C", CLOCK_2, LATCH_2, DATA_2))
motors.append(Motor("E", "F", CLOCK_3, LATCH_3, DATA_3))
motors.append(Motor("F", "E", CLOCK_3, LATCH_3, DATA_3))

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

def main():
    try:
        for motor in motors:
            motor.reset()
        #motors[4].move("up", 0.195, 40)
        motors[5].move("down", 0.175, 40)
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError as err:
                if 'cannot join current thread' in err:
                    continue
                else:
                    raise
        GPIO.cleanup()

    except KeyboardInterrupt:
        print "exiting"
        GPIO.cleanup()
    sys.exit(0)

main()

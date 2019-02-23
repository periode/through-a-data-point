import sys
import RPi.GPIO as GPIO
import time
import threading
from subprocess import Popen

# NOTES

GPIO.setmode(GPIO.BCM)

MOTOR_A_A = 18
MOTOR_A_B = 23
MOTOR_A_C = 24
MOTOR_A_D = 25

MOTOR_B_A = 4
MOTOR_B_B = 17
MOTOR_B_C = 27
MOTOR_B_D = 22

MOTOR_C_A = 12
MOTOR_C_B = 16
MOTOR_C_C = 20
MOTOR_C_D = 21

MOTOR_D_A = 6
MOTOR_D_B = 13
MOTOR_D_C = 19
MOTOR_D_D = 26



class Motor:
    def __init__(self, _id, _a, _b, _c, _d):
        self.id = _id
        self.pins = [_a, _b, _c, _d]

    def setStep(self, values):
        GPIO.output(self.pins[0], values[0])
        GPIO.output(self.pins[1], values[1])
        GPIO.output(self.pins[2], values[2])
        GPIO.output(self.pins[3], values[3])

    def up(self, delay, steps):
        for i in range(0, steps):
            self.setStep([1, 0, 1, 0])
            time.sleep(delay)
            self.setStep([0, 1, 1, 0])
            time.sleep(delay)
            self.setStep([0, 1, 0, 1])
            time.sleep(delay)
            self.setStep([1, 0, 0, 1])
            time.sleep(delay)


    def down(self, delay, steps):
        for i in range(0, steps):
            self.setStep([1, 0, 0, 1])
            time.sleep(delay)
            self.setStep([0, 1, 0, 1])
            time.sleep(delay)
            self.setStep([0, 1, 1, 0])
            time.sleep(delay)
            self.setStep([1, 0, 1, 0])
            time.sleep(delay)

    def move(self, dir, delay, steps):
        if dir == "up":
            t = threading.Thread(target=self.up, args=(delay, steps))
            t.start()
        else:
            t = threading.Thread(target=self.down, args=(delay, steps))
            t.start()

    def reset(self):
        self.setStep([0, 0, 0, 0])

motors = []

motors.append(Motor("A", MOTOR_A_A, MOTOR_A_B, MOTOR_A_C, MOTOR_A_D))
motors.append(Motor("B", MOTOR_B_A, MOTOR_B_B, MOTOR_B_C, MOTOR_B_D))
motors.append(Motor("C", MOTOR_C_A, MOTOR_C_B, MOTOR_C_C, MOTOR_C_D))
motors.append(Motor("D", MOTOR_D_A, MOTOR_D_B, MOTOR_D_C, MOTOR_D_D))

GPIO.setup(MOTOR_A_A, GPIO.OUT)
GPIO.setup(MOTOR_A_B, GPIO.OUT)
GPIO.setup(MOTOR_A_C, GPIO.OUT)
GPIO.setup(MOTOR_A_D, GPIO.OUT)

GPIO.setup(MOTOR_B_A, GPIO.OUT)
GPIO.setup(MOTOR_B_B, GPIO.OUT)
GPIO.setup(MOTOR_B_C, GPIO.OUT)
GPIO.setup(MOTOR_B_D, GPIO.OUT)

GPIO.setup(MOTOR_C_A, GPIO.OUT)
GPIO.setup(MOTOR_C_B, GPIO.OUT)
GPIO.setup(MOTOR_C_C, GPIO.OUT)
GPIO.setup(MOTOR_C_D, GPIO.OUT)

GPIO.setup(MOTOR_D_A, GPIO.OUT)
GPIO.setup(MOTOR_D_B, GPIO.OUT)
GPIO.setup(MOTOR_D_C, GPIO.OUT)
GPIO.setup(MOTOR_D_D, GPIO.OUT)


def main():
    try:
        for motor in motors:
            motor.reset()

        Popen(['/usr/bin/omxplayer', 'legal_1-0.mp4'])        
        motors[0].move("up", 0.075, 40)
        motors[1].move("down", 0.025, 40)
        motors[2].move("down", 0.055, 40)
        motors[3].move("up", 0.085, 40)

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

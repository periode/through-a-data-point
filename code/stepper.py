import RPi.GPIO as GPIO
import time

coil_A_1_pin = 18 #white, goes to input 3
coil_B_1_pin = 23 #green, goes to input 4
coil_A_2_pin = 24 #orange, goes to input 2
coil_B_2_pin = 25 #yellow, goes to input 1

# OUTPUT
# output 1 is yellow cable
# output 2 is orange cable
# output 3 is green cable
# output 4 is blue cable

# GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# GPIO.output(enable_pin, 1)

def forward(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

def backwards(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)


def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

print "hello"
time.sleep(1)

while True:
  delay = raw_input("pick a delay between steps (in ms, 10ms makes it go pretty fast)? ")
  steps = raw_input("going forward: how many steps? ")
  forward(int(delay) / 1000.0, int(steps))
  steps = raw_input("and now backward: how many steps? ")
  backwards(int(delay) / 1000.0, int(steps))
  choice = raw_input("continue? [y/n] ")
  if choice == 'n':
      GPIO.cleanup()
      break

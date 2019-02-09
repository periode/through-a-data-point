# through-a-data-point
Code + doc for Data Through Design 2019

## HARDWARE

- 6x [Stepper Motor](https://www.sparkfun.com/products/10848)
- 6x [L293D Driver IC](https://www.engineersgarage.com/electronic-components/l293d-motor-driver-ic)
- 3x [74HC595N Shift Register](https://www.sparkfun.com/products/13699)
- 1x [Raspberry Pi Model 3B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- 1x Power Supply DC 12V 0.6A
- 1x [Power Connector](https://ftaelectronics.com/image/cache/catalog/RG6%20Cable%20and%20Connectors/Cat6%20Connectors/2Pcs%20CCTV%20Camera%20UTP%20Power%20DC%20Plug%202.1mm%205.5mm%20Female%20Power%20Connectors-1024x768_0.jpg)
- 1x MicroSD Card 16GB

## SETUP

### Wiring

The diagram for wiring a **single motor** can be found [here](https://github.com/periode/through-a-data-point/tree/master/resources/single_stepper_diagram.pdf).

Things to take into consideration:
- The power source is represented as 2x AA Batteries. It should instead be the 12V power supply, connected to the [power connector](https://ftaelectronics.com/image/cache/catalog/RG6%20Cable%20and%20Connectors/Cat6%20Connectors/2Pcs%20CCTV%20Camera%20UTP%20Power%20DC%20Plug%202.1mm%205.5mm%20Female%20Power%20Connectors-1024x768_0.jpg).
- The wires coming out of the stepper motor are black and red. For clarity, I've connected them to wires that are the same as their actual color (red, green, yellow, blue).
  - This means that red and yellow go on one side of the IC, while green and blue should go on the other side.

## Programming

In order to set up the raspberry pi, you will need to **install** it, **find** it, **connect** to it and **execute** the sample program.

1. Download the [disk image]() that we will flash on the SD card.
2. Download [Etcher](https://www.balena.io/etcher/).
3. Insert the SD card in your computer.
4. Open Etcher, select the image you just downloaded and the SD card you just inserted, and flash.
5. Insert the microSD card in the raspberry pi and connect it to a power source. A microUSB plugged in to a laptop is enough.
6. Once the raspberry pi is powered up, you should see a solid blinking LED.
7. On your computer, open the Command Prompt and type `ping raspberrypi`. The [output](http://j.tlns.be/wp-content/uploads/2015/02/step2_ping.png) should give you the IP address of the raspberry pi.
8. Download [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (you probably want the 64bit MSI version).
9. Enter the IP address of the raspberry pi in the `Host Name (or IP address)` field, with `Port` set to 22 and click `Open`.
10. A command prompt should open. When asked to login as, enter `pi` and for password enter `raspberry`.
11. You are now connected to the raspberry pi. To execute the code to make the stepper motor turn, type `python stepper.py` and press `ENTER`. Follow the prompts on the screen to select the delays/numbers of rotations.

import serial #sudo apt install python-serial
import sys
from subprocess import Popen

ser = serial.Serial('/dev/ttyACM0', 9600)

def main():
    try:
        while True:
            read_serial = ser.readline()
            #print read_serial
        
            if "reached top" in read_serial:
                print "the motors have reached the top, stopping video..."
                # stop the video
                Popen(['pkill', '-9', 'omxplayer'])
            elif "reached bottom" in read_serial:
                print "the motors have reached the bottom, playing video..."
                # play the video
                Popen(['/usr/bin/omxplayer', '-b', 'legal_landscape.mp4'])


    except KeyboardInterrupt:
        print "exiting"
    sys.exit(0)

main()

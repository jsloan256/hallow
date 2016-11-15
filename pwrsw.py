import sys
import time
import RPi.GPIO as gpio
import argparse

parser = argparse.ArgumentParser(description='Set PS switch state')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer defining the PS state')
parser.add_argument('--state', dest='state', action='store_const',
                    const=sum, default=max,
                    help='Set the PS switch state (default: 2, pulse)')

args = parser.parse_args()
#print args.state(args.integers)



# Use Rapberry Pi BOARD pin numbers
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) 

gpio.setup(11, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

# OFF
gpio.output(11, gpio.HIGH)
gpio.output(12, gpio.HIGH)

time.sleep(3)

# ON
gpio.output(11, gpio.LOW)
gpio.output(12, gpio.LOW)

#while (1):
#  time.sleep(1)
#  gpio.output(11, gpio.LOW)
#  gpio.output(12, gpio.LOW)

#  time.sleep(1)
#  gpio.output(11, gpio.HIGH)
#  gpio.output(12, gpio.HIGH)


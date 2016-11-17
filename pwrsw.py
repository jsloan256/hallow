import sys
import time
import RPi.GPIO as gpio
import argparse

parser = argparse.ArgumentParser(description='Set PS switch state')
parser.add_argument('--state', dest='state',
                    default='cycle',
                    help='Set the PS switch state (cycle, on, off)')

args = parser.parse_args()

# Use Rapberry Pi BOARD pin numbers
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) 
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

# Operate the IoT power switch based on the 'state' argument
if (args.state == 'cycle'):

  # OFF
  gpio.output(11, gpio.HIGH)
  gpio.output(12, gpio.HIGH)

  time.sleep(3)

  # ON
  gpio.output(11, gpio.LOW)
  gpio.output(12, gpio.LOW)

elif (args.state == 'on'):

  # ON
  gpio.output(11, gpio.LOW)
  gpio.output(12, gpio.LOW)

elif (args.state == 'off'):

  # OFF
  gpio.output(11, gpio.HIGH)
  gpio.output(12, gpio.HIGH)


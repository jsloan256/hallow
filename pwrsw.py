import socket
import sys
import time
import RPi.GPIO as gpio
import pygame

def play_audio(fn, times):
  for i in range(0, times):
#    pygame.mixer.Sound.set_volume(.5)
    pygame.mixer.music.load(fn)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
      continue

## Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
## Connect the socket to the port on the server given by the caller
#server_address = ('tweedle.hallow.local', 10000)
#print >> sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)
#
#try:
#    
#  message = 'This is the message.  It will be repeated.'
#  print >>sys.stderr, 'sending "%s"' % message
#  sock.sendall(message)
#
#  amount_received = 0
#  amount_expected = len(message)
#  while amount_received < amount_expected:
#    data = sock.recv(16)
#    amount_received += len(data)
#    print >>sys.stderr, 'received "%s"' % data
#
#finally:
#  sock.close()

# Use Rapberry Pi BOARD pin numbers
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) 

gpio.setup(11, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

pygame.mixer.init()

gpio.output(11, gpio.LOW)
gpio.output(12, gpio.LOW)

while (1):

  gpio.output(11, gpio.LOW)
  gpio.output(12, gpio.LOW)
  play_audio('zombie.mp3', 1)
  gpio.output(12, gpio.HIGH)
  time.sleep(10)
  gpio.output(12, gpio.LOW)
  play_audio('scary.mp3', 1)
  gpio.output(12, gpio.HIGH)
  time.sleep(3)
  play_audio('laugh.mp3', 1)
  time.sleep(3)
  gpio.output(11, gpio.HIGH)
  time.sleep(7)

#  play_audio('bat.mp3')
#  play_audio('scary.mp3')
#  play_audio('zombie.mp3')
#  play_audio('laugh.mp3')


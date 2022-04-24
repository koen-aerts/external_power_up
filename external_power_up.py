#!/usr/bin/env python3
from gpiozero import LED 
from time import sleep

trigger_pin = LED(23) 

try:
  trigger_pin.off()
  while 1:
    sleep(3600)
except KeyboardInterrupt:
  pass

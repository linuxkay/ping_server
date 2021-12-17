#!/usr/bin/env/python
#This python script is to check server is alive or not by ping
import time
import os
hostname = "PUT TARGET IP or HOSTNAME"
response = os.system("ping -c 1 " + hostname)

#and then check the response...
#while True:
if response == 0:
  time.sleep(3)
  os.system("mpg123 sounds/beep-07.mp3")
  print hostname, 'is up!'
else:
  os.system("mpg123 sounds/beep_down.mp3")
  time.sleep(1.2)
  print hostname, 'is down!'

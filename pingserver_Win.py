#!/usr/bin/env/python3
#This python script is to check server is alive or not by ping
import time
import os
import playsound
hostname = input("Enter HostName/IP: ")

while True:
  response = os.system("ping -n 1 " + hostname)
  if response == 0:
      time.sleep(3)
      playsound.playsound('sounds/beep-07.mp3')
      print(hostname, 'is Alive')
  else:
      playsound.playsound('sounds/beep_down.mp3')
      time.sleep(1.2)
      print(hostname, 'is down!')

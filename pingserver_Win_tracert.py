#!/usr/bin/env/python3
#This python script is to run tracert on windows if the target host is down.
# build by ohnuma@
import time
import subprocess
import os
import asyncio
import time

# Let user type hostname
hostname = input("Enter HostName/IP: ")

# Set timestring for saving file.
timestr = time.strftime("%Y%m%d-%H%M%S")

# Save file for  example1.com
output_file1 = timestr + 'tracert_example1.txt'
# Save fike for exmaple2.com
output_file2 = timestr + 'tracert_exmaple2.txt'

# Asynchronous tasks to traceroute 2 hostname at same time.
async def main():
    # tracertoute for example1.com
    task1 = asyncio.create_task(tracert_example1())
    # traceroute for exmaple2.com
    task2 = asyncio.create_task(tracert_exmaple2())
    # Wait task1 to finish.
    await task1
    # Wait task2 to finish.
    await task2

# example1.com async def.
async def tracert_example1():
    print('tracert_example1() started')
with open(output_file1, 'w') as f:
    subprocess.Popen("tracert example1.com", stdout=f)

# exmaple2.com async def.
async def tracert_exmaple2():
    print('tracert_exmaple2() started')
with open(output_file2, 'w') as f:
    subprocess.Popen("tracert exmaple2.com", stdout=f)

# Loop for ping.
while True:
  response = os.system("ping -n 1 " + hostname)
  if response == 0:
      time.sleep(3)
      print(hostname, 'is Alive')
  else:
      print(hostname, 'is down!')
      # Initiate asny def.
      asyncio.run(main())
      time.sleep(1.2)

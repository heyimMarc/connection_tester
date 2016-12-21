#!/usr/bin/env python
import csv
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open('connections.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
        result = sock.connect_ex((row[0],int(row[1])))
        if result == 0:
            print "Works: " + row[0] + ":" + row[1]   
        else:
            print "Not working: " + row[0] + ":" + row[1] 
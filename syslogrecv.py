#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('127.0.0.1', 514)
print "start syslog receiver on %s port %s" % server_addr
sock.bind(server_addr)

while True:
    data, address = sock.recvfrom(4096)
    if data:
        print data

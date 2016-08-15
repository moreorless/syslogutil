#!/usr/bin/python

import sys, time, random
from socket import *

if len(sys.argv) < 3:
    print 'Usage: send2syslog [ip] [port]'
    sys.exit()

host = sys.argv[1]
textport = sys.argv[2]

#
totalcount = 0
maxlines = 100

udpSock = socket(AF_INET, SOCK_DGRAM)

try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')
ADDR = (host, port)


starttime = time.time()
filename = 'sample.log'

try:
    while True:
        with open(filename) as fp:
            for line in fp:
                print totalcount, "---", line
                totalcount += 1
                udpSock.sendto(line, ADDR)
                time.sleep(random.random())

        if totalcount >= maxlines:
            break
        time.sleep(random.randint(1, 5))


except Exception, e:
    print "Error: ", e

endtime = time.time()


print "start time : ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
print "end time : ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endtime))
timeused = (endtime - starttime)
print "time used : " + str(timeused) + "s, eps = " + str(totalcount / timeused)

udpSock.close()

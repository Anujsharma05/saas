#!/usr/bin/python

import os,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.82"
#server's IP

s_port=9999

os.system('ssh -X test@' + s_ip + ' cheese')
execfile('saas.py')


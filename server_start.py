#!/usr/bin/python
import socket,os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",9999))

c_data=s.recvfrom(100)
#it stores the client's username

c_data1=s.recvfrom(100)
#it stores the client's password

if c_data[0]=='test' and c_data1[0]=='123':
	print "Connection successful"
	s.sendto("ok",c_data[1])
else:
	print "connection failed"
	s.sendto("not ok",c_data[1])

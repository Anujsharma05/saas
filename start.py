#!/usr/bin/python
import socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.82"
#server IP

s_port=9999
#common port

print "Cloud Service has started , Please enter authentication details"

s_user=raw_input("enter your username: ")
#it will store server's username

s_pass=getpass.getpass()
#it will store server's password

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_pass,(s_ip,s_port))

s_data=s.recvfrom(2)

if s_data[0]=="ok":
	print "connection is ready"
	print "wait for service to start"
	execfile('saas.py')
else:
	print "check your username or password"
	exit()

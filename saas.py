#!/usr/bin/python

x="""
print 1 to open Firefox
print 2 to open Calculator
print 3 to open Screenshot
print 4 to open Webcam
print 5 to open Image Viewer
print 6 to start LibreOffice
print 7 to open VLC
"""

print x 

choice=raw_input()

if choice=='1':
	print "firefox is about to run"
	execfile('firefox.py')
elif choice =='2':
	print "calculator is abour to run"
	execfile('calculator.py')
elif choice=='3':
	print "screenshot is about to run"
	execfile('screenshot.py')
elif choice=='4':
	print "webcam is about to run"
	execfile('webcam.py')
elif choice=='5':
	print "Image viewer is about to run"
	execfile('viewer.py')
elif choice=='6':
	print "LibreOffice is about to run"
	execfile('offcie.py')
elif choice=='7':
	print "VLC is about to run"
	execfile('vlc.py')
else:
	print "wrong choice"

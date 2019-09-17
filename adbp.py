#!/usr/bin/env python 
import os
runshell  =  '/opt/genymobile/genymotion/tools/adb shell'
rundevice =  '/opt/genymobile/genymotion/tools/adb devices'
runlog =  '/opt/genymobile/genymotion/tools/adb logcat > log.txt'
print ('''
--  1____11_____11___11____11____11____11_____11_11_1
--  (11_1\(11_11)/1__)(1___)(_11_)(11_1\(11_11)(1\(1)
--  1)___/1)(_)(1\__1\1)__)11_)(_11)(_)1))(_)(11)11(1
--  (__)11(_____)(___/(____)(____)(____/(_____)(_)\_)
	''')
print """
	  Entet run  to  Adb-Shell
	  Enter device to  Adb-Device
	  Enter runlog to  Log
	  cat log.txt | grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b"
	  ./tcpdump -i any(interface) -s0 -n -w /sdcard/out.pcap
	  strings -n 6 out.pcap | grep -i "(asu like)"

"""
input = raw_input("Enter --> ")
if input == 'run':
	os.system(runshell)
elif input == 'device':
	os.system(rundevice)
elif input == 'runlog':
	os.system(runlog)
else:
	print "Something  Worng"





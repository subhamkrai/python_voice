#!/usr/bin/python

import  thread
import time
def  ok():

	while True:
		print  "okey Google"
		time.sleep(2)

def   notok():

	while True:
		print  "okey facebook"
		time.sleep(3)


thread.start_new_thread(ok,())
thread.start_new_thread(notok,())

while True:
	pass

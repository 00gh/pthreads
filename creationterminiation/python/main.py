#!/usr/bin/python

import threading
import time
import socket
#from tqdm import tqdm


# Define a function for the thread
def print_time(threadName, delay, numreps):
	count = 0
	while count < numreps:
		count += 1
        #print "%i) %s" % (count, threadName)
		print ("%s: %s" % (threadName, time.ctime(time.time())))
		time.sleep(delay)

	return

def hello(t_id, delay):
	print("Hello from thread", t_id, "my name is:", threading.currentThread().getName())
	time.sleep(delay)
	print("Exit", threading.currentThread().getName())
	return
	
# Create two threads as follows
try:
	threads = []
	t1 = threading.Thread(name="Thread 1", target = hello, args=(1, 3))
	t2 = threading.Thread(name="Thread 2", target = hello, args=(2, 10))
	threads.append(t1)
	threads.append(t2)
	t1.start()
	t2.start()
	t2.join()
	t_time = threading.Thread(name = "Time thread", target = print_time("Time lord", 2, 3))
	t_time.start()
	
except:
    print ("Error: unable to start thread")
    


#def process(item):
#	time.sleep(0.1)
	
#items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for item in tqdm(items):
#	process(item)
	
#for i in tqdm(range(1000)):
#	time.sleep(0.01)
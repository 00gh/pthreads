#!/usr/bin/python

import threading
import time

NUM_THREADS = 5

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


def BusyWork(t_id):
	print("Thread id: ", t_id, " heading for sleep")
	time.sleep(6)
	print(t_id, " awake")
	return
	
# Create two threads as follows
try:
	threads = []
	
	print("Starting threads")
	for i in range(NUM_THREADS):
		t =  threading.Thread(name="Worker",   target = BusyWork, args=(i, ))
		threads.append(t)
		t.start()
		
	# Wait till awake
	t.join()
	print("Exiting")
	
except:
    print ("Error: unable to start thread")
    


#def process(item):
#	time.sleep(0.1)
	
#items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for item in tqdm(items):
#	process(item)
	
#for i in tqdm(range(1000)):
#	time.sleep(0.01)
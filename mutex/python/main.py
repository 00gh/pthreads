#!/usr/bin/python

import threading
import time
#import tqdm

NUM_THREADS = 9

class data:
	def __init__(self):
		self.lock = threading.Lock()
		self.value1 = 0
		self.value2 = 0


def BusyWork(t_id):
	print("Thread id: ", t_id, " waiting for lock")
	my_data.lock.acquire()
	print("Thread id: ", t_id, "Lock acquired. Value 1 = ", my_data.value1)
	my_data.value1 += my_data.value2
	time.sleep(5.5)
	print("Thread: ", t_id, " releasing lock")
	my_data.lock.release()
	return
	
# Create two threads as follows
try:
	my_data = data()
	my_data.value2 = 1
	threads = []
	
	print("Starting threads")
	for i in range(NUM_THREADS):
		t =  threading.Thread(name="Worker",   target = BusyWork, args=(i, ))
		threads.append(t)
		t.start()
		
			
	t.join()
	print("Exiting")
	
#	s.value1 = 10
	
except:
    print ("Error: unable to start thread")
    


#def process(item):
#	time.sleep(0.1)
	
#items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for item in tqdm(items):
#	process(item)
	
#for i in tqdm(range(1000)):
#	time.sleep(0.01)

'''
pythonic module threading calls underlying cumbersome lib thread
as Java, there are several ways to create thread in python

this example illustrute first one
'''

import threading 
import time

def worker():
    ''' get thread name and sleep 2 sec '''
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service) #name a thread, pass target
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name


t.setDaemon(True) #set this process as daemon

w.start()
w2.start()
t.start()

main_thread = threading.currentThread()
#enumerate function let you list all threads in current space
for t in threading.enumerate():
    if t is not main_thread:
        print "I have ", t.getName()

t.join() # will until thread t to finish

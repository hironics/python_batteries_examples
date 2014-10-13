
'''
there are lots of synchronize methanism within python
threading

Lock
RLock
Event
'''
import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker_with(lock):
    ''' lock supports with context manager'''

    with lock:
        logging.debug('Lock acquired via with')
        
def worker_no_with(lock,rlock):
    ''' typical lock manuplate
    acquire
    release
    '''
    lock.acquire()
    rlock.acquire()
    rlock.acquire() #re entry lock allows acquire a lock as many times as you need
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

lock = threading.Lock() #create a lock
rlock = threading.RLock() #create a rlock
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,rlock))

w.start()
nw.start()


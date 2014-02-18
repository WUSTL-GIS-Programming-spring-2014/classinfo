#!/usr/bin/env python
import threading
import time
import random
 
class MyThread(threading.Thread):
    def run(self):
        print("%s started!" % self.getName())              # "Thread-x started!"
        time.sleep(2*random.random())                       # Pretend to work for a second
        print("%s finished!" % self.getName())             # "Thread-x finishsed!"
 
if __name__ == '__main__':
    for x in range(6):                                     # Four times...
        mythread = MyThread(name = "Thread-%d" % (x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(random.random())                        # ...Wait 0.9 seconds before starting another
        

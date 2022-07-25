import threading
import time as t
class DemoThread(threading.Thread):
    def __init__(self,input1):
        for i in input1:
            print(i,ord(i))
d=DemoThread("Thread 1")
import threading, time
def fun1(name):
  print("Starting",name)
  time.sleep(2) # Sleeps for 2 Sec
  print("Finishing",name)

x = threading.Thread(target=fun1,args=("Thread 1",))
x.start()
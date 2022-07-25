from threading import Thread, Lock
from time import sleep


class PrimeThread(Thread):
    def __init__(self, input1, l):
        l.acquire()
        print(input1, end=" ")
        for i in range(2, input1):
            if input1 % i == 0:
                sleep(1)
                print("Not prime")
                break
        else:
            print("Prime")
        l.release()


class OddPrime(Thread):
    def __init__(self, input1, l):
        l.acquire()
        print(input1, end=" ")
        if(input1 % 2 != 0):
            print("Odd", end="")
            p1 = PrimeThread(input1)
        else:
            print("Not OddPrime")
        l.release()


l = Lock()
t1 = Thread(target=PrimeThread, args=(3, l))
t2 = Thread(target=OddPrime, args=(2, l))
t1.start()
t2.start()
t1.join()
t2.join()

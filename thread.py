import threading
import time


def my_fun(n):
    print "Starting thread no.",n
    time.sleep(3)
    print "Ending thread no.",n

threads = []
for i in range(5):
    my_fun(i)
    threads.append(i)
print threads
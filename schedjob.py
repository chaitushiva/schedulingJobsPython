import time
import datetime

def job():
    print (datetime.datetime.now())

try:
    count = 1
    while (count<10):
        job()
        time.sleep(3)
        count = count+1

except KeyboardInterrupt:
    print ("Key interrupt")




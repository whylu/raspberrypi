import sys
sys.path.append("./DHT11_Python-master")

import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime
import calendar

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read pin from argv
if(len(sys.argv)==1):
    print "need argv[1] for <pin>"
    sys.exit()

pin = sys.argv[1]
#read data using pin 
instance = dht11.DHT11(int(pin))


while True:
    result = instance.read()
    if result.is_valid():
        utcnow = datetime.utcnow()
        with open('/tmp/pi_dht11_4', 'w') as the_file:
            #write file as fomat: <Temperature>, <Humidity>, <UTC+0000 in second in epoch>
            the_file.write("{}, {}, {}\n".format(result.temperature, result.humidity, calendar.timegm(utcnow.utctimetuple())))
        
    time.sleep(1)


import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("LSB", "MSB")

hx.set_reference_unit(92)

hx.reset()
hx.tare()

file = open("values.txt","w")
avgBin = 10        

values = []

while True:
    try:
        #Finds the average of weights
        values.append(hx.get_weight(30))
        print("Value "+str(x.get_weight(30)))

        avg = sum(values) / float(len(values))

        print("Avg "+str(avg))

        file.write(str(avg))
        #print(avg)
        
        #print(hx.get_weight(30))

        hx.power_down()
        hx.power_up()
        time.sleep(0.2)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        file.close()

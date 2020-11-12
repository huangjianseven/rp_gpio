from gpiozero import LED 
from time import sleep 

red = LED(17) 
 
while True: 
    red.on()    #turn led on 
    sleep(1)    #delay for 1 second 
    red.off()   #turn led off 
    sleep(1)
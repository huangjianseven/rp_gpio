import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT) 
p = GPIO.PWM(17, 100)    # 100 is frequency 
dc = 0 
p.start(dc)   # where dc is the duty cycle (0.0 <= dc <= 100.0) 
for x in range(3): 
    for i in range(0, 10): 
        dc += 10 
        p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0 
        sleep(0.2) 
 
    for i in range(0, 10): 
        dc -= 10 
        p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0 
        sleep(0.2) 
p.stop() 
GPIO.cleanup() 

from gpiozero import PWMLED 
from time import sleep 
led = PWMLED(17) 
while True: 
        led.value = 0    # off 
        sleep(1) 
        led.value = 0.2  # 20% brightness 
        sleep(1) 
        led.value = 0.4  # 40% brightness 
        sleep(1) 
        led.value = 0.6  # 60% brightness 
        sleep(1) 
        led.value = 1    # full brightness 
        sleep(1) 

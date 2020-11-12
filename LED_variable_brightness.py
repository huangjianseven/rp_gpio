from gpiozero import PWMLED 
from signal import pause 
 
led = PWMLED(17) 
led.pulse(1,1,5) #fade_in in 1s, fade_out in 1s, do it for 3 times 
pause() 

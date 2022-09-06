# PIR sensor test

import wiringpi
import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 0) # Use pin as INPUT

while True:
    value = wiringpi.digitalRead(21)
    print(value)
    time.sleep(0.5) # s

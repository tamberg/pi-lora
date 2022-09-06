# PIR sensor test
# $ pip3 install gpiozero

import time
from gpiozero import MotionSensor

pir = MotionSensor(22)

while True:
    print(pir.motion_detected)
    time.sleep(0.5) # s


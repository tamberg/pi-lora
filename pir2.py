# PIR sensor test 2
# $ pip3 install gpiozero

import time
from gpiozero import MotionSensor

pir = MotionSensor(22)

while True:
    if pir.motion_detected:
        print("sending notification...") # TODO: send actual data
        time.sleep(6) # TODO: increase to 60 s or more
    else:
        print("no motion detected")
        time.sleep(0.5) # s


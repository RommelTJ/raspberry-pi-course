from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4)

while True:
    sleep(0.01)
    print(pir.motion_detected)

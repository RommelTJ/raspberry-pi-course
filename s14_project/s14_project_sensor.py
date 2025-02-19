from os import path
from gpiozero import LED, MotionSensor
from signal import pause
from picamzero import Camera
from time import sleep

# TODO: When the sensor detects motion greater than 5 seconds, it will turn on the LED
# TODO: When the sensor detects motion greater than 5 seconds, take a photo and send an email
# TODO: For each photo that we take, log the time and filename into a log file.

class MotionActivatedCamera:
    def __init__(self):
        self.light = LED(17)
        self.pir_sensor = MotionSensor(4)
        self.camera = Camera()
        self.camera.still_size = (1536, 864)
        self.camera.flip_camera(hflip=True, vflip=True)
        print("Initializing camera...")
        sleep(2) # Wait for the camera to initialize
        print("Camera initialized!")
        self.pir_sensor.when_motion = self.turn_light_on
        self.pir_sensor.when_no_motion = self.turn_light_off

    def turn_light_on(self):
        self.light.on()

    def turn_light_off(self):
        self.light.off()

    def run(self):
        try:
            pause()
        except KeyboardInterrupt:
            print("Exiting gracefully")

if __name__ == '__main__':
    c = MotionActivatedCamera()
    c.run()

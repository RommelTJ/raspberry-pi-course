from os import path
from gpiozero import LED, MotionSensor
from signal import pause
from picamzero import Camera
from time import sleep, time

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
        self.pir_sensor.when_motion = self.on_motion_detected
        self.pir_sensor.when_no_motion = self.on_motion_finished
        self.time_of_first_motion = 0
        self.last_photo_time = 0
        self.MOVEMENT_THRESHOLD_SECONDS = 5
        self.MIN_SECONDS_BETWEEN_PHOTOS = 30

    def on_motion_detected(self):
        self.light.on()
        self.time_of_first_motion = time()

    def on_motion_finished(self):
        self.light.off()
        motion_duration = time() - self.time_of_first_motion
        print(f"Motion duration: {motion_duration} seconds")
        if motion_duration > self.MOVEMENT_THRESHOLD_SECONDS:
            can_take_photo = time() - self.last_photo_time > self.MIN_SECONDS_BETWEEN_PHOTOS
            if can_take_photo:
                self.take_photo()
                self.last_photo_time = time()

    def take_photo(self):
        print("Taking photo...")

    def run(self):
        try:
            pause()
        except KeyboardInterrupt:
            print("Exiting gracefully")

if __name__ == '__main__':
    c = MotionActivatedCamera()
    c.run()

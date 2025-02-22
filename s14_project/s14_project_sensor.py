from os import path, mkdir
from gpiozero import LED, MotionSensor
from signal import pause
from picamzero import Camera
from time import sleep, time
import yagmail


class MotionActivatedCamera:
    def __init__(self, photo_dir: str, log_dir: str):
        self.light = LED(17)
        self.pir_sensor = MotionSensor(4)
        self.camera = Camera()
        self.camera.still_size = (1536, 864)
        self.camera.flip_camera(hflip=True, vflip=True)
        self.photo_dir = photo_dir
        self.ensure_dir(self.photo_dir)
        self.log_dir = log_dir
        self.ensure_dir(self.log_dir)
        print("Initializing camera...")
        sleep(2) # Wait for the camera to initialize
        print("Camera initialized!")
        self.pir_sensor.when_motion = self.on_motion_detected
        self.pir_sensor.when_no_motion = self.on_motion_finished
        self.time_of_first_motion = 0
        self.last_photo_time = 0
        self.MOVEMENT_THRESHOLD_SECONDS = 5
        self.MIN_SECONDS_BETWEEN_PHOTOS = 30
        self.email_password = ""
        with open("/home/pi/Desktop/code/gmail_password.txt", "r") as f:
            self.email_password = f.read().rstrip()

    def ensure_dir(self, dir_path: str):
        if not path.exists(dir_path):
            mkdir(dir_path)

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
        timestamp = str(time())
        filename = f"{self.photo_dir}/photo_{timestamp}.jpg"
        self.camera.take_photo(filename)
        self.write_to_log(message=filename)
        self.send_email()

    def write_to_log(self, message: str):
        filename = f"{self.log_dir}/log.txt"
        with open(filename, "a") as f:
            f.write(f"{message}\n")

    def latest_photo_from_log(self):
        filename = f"{self.log_dir}/log.txt"
        with open(filename, "r") as f:
            lines = f.readlines()
            return lines[-1].rstrip()

    def send_email(self):
        print("Sending email...")
        latest_photo_path = self.latest_photo_from_log()
        from_email = "[REDACTED]@gmail.com"
        to_email = "[REDACTED]@gmail.com"
        yag = yagmail.SMTP(user=from_email, password=self.email_password)
        yag.send(
            to=to_email,
            subject="Movement detected",
            contents="The camera took a photo",
            attachments=latest_photo_path
        )

    def run(self):
        try:
            pause()
        except KeyboardInterrupt:
            print("Exiting gracefully")

if __name__ == '__main__':
    c = MotionActivatedCamera(
        photo_dir="/home/pi/Desktop/final/img",
        log_dir="/home/pi/Desktop/final/logs"
    )
    c.run()

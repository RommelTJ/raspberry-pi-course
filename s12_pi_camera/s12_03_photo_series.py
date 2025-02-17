from os import path
from time import sleep
from picamzero import Camera

class PhotoSeries:
    def __init__(self, photo_dir: str, interval_seconds: int = 5):
        self.photo_dir = photo_dir
        self.interval_seconds = interval_seconds
        self.camera = Camera()
        self.camera.still_size = (1536, 864)
        self.camera.flip_camera(hflip=True, vflip=True)
        self.photo_count = 0
        self.ensure_dir(self.photo_dir)
        print("Initializing camera...")
        sleep(2) # Wait for the camera to initialize
        print("Camera initialized!")


    def ensure_dir(self, dir_path: str):
        if not path.exists(dir_path):
            os.mkdir(dir_path)

    def take_photo(self):
        filename = f"{self.photo_dir}/photo_{self.photo_count}.jpg"
        self.camera.take_photo(filename)
        self.photo_count += 1
        print(f"Photo taken: {filename}")

    def run(self):
        try:
            while True:
                self.take_photo()
                sleep(self.interval_seconds)
        except KeyboardInterrupt:
            print("Exiting gracefully")


if __name__ == '__main__':
    camera = PhotoSeries(photo_dir="/home/pi/Desktop/camera/photo_series", interval_seconds=5)
    camera.run()

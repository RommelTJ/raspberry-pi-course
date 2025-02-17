from picamzero import Camera
from time import sleep

camera = Camera()
camera.still_size = (1536, 864)
camera.flip_camera(hflip=True, vflip=True)
sleep(2) # Wait for the camera to initialize

# Take a photo
camera.take_photo('/home/pi/Desktop/camera/test3.jpg')
print("Photo taken")

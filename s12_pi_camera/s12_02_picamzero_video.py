from picamzero import Camera
from time import sleep

camera = Camera()
camera.video_size = (640, 480)
camera.flip_camera(hflip=True, vflip=True)
sleep(2) # Wait for the camera to initialize

# Take a video
print("Video recording...")
camera.record_video('/home/pi/Desktop/camera/test4.mp4', 7)
print("Video taken")

# Add Vision to Your Applications with the Raspberry Pi Camera

* Important difference for the cables
    * The Raspberry Pi 4 needs 15 pin (1mm) cables. You connect it directly to the Pi.
    * The Raspberry Pi 5 needs 22 pin (0.5mm) cables. You may need a new cable (15 pin to 22 pin).

## Plug the Camera to your Raspberry Pi

* Open the Pi ports (black cover). Connect the cables with the blue facing the USB ports. Make sure the Pins are tight.
  * https://www.escogitare.com/blog/en/connect_camera_to_raspberry
* Instructions are different for the Pi 5.

## Take a Photo from the Terminal

* Make a directory for the photos (`/home/pi/Desktop/camera`)
* `rpicam-still -o /home/pi/Desktop/camera/test.jpg`
  * To flip, use `--vflip`
  * To rotate, use `--hflip`
  * To change size, use `--width 1536 --height 864` (for example)
  * Together: `rpicam-still --vflip --hflip --width 1536 --height 864 -o /home/pi/Desktop/camera/test.jpg`
* `libcamera-jpeg --list-cameras`
* `libcamera-jpeg -o /home/pi/Desktop/camera/test.jpg –immediate`
* `libcamera-jpeg` is older and not recommended. Use `rpicam-still` instead.

## Take a Video from the Terminal

* Similar to the photo.
* `rpicam-vid -o /home/pi/Desktop/camera/test.mp4` (by default it's 5 seconds).
* `rpicam-vid --vflip --hflip --width 640 --height 480 -t 7000 -o /home/pi/Desktop/camera/test.mp4`
* Time is in milliseconds.
* `rpicam-vid --codec libav --libav-format mp4 --vflip --hflip --width 640 --height 480 -t 7000 -o /home/pi/Desktop/camera/test2.mp4`
* For more details, see https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-vid.

## Take a Photo with Python

* Using `picamzero` module
* Install it: `sudo apt update && sudo apt install python3-picamzero`
* See `s12_01_picamzero.py`

## Take a Video with Python

* Very similar to photos.
* See `s12_02_picamzero_video.py`

## Take a Series of Pictures

* Take a series of photos every 5 seconds, until the user cancels the program.
* Put the photos in a new directory. We should create it if it doesn't exist.
* Photos should always have different names.
* See `s12_03_photo_series.py`

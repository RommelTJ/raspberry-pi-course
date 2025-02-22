# Final Project

* You will have two files.
* The first will be a Python program for configuring the Pi.
  * When the sensor detects motion, it will turn on the LED, take a photo, and send an email with the photo.
  * Configuring the PIR sensor.
  * Configuring the camera.
  * Write data into a log file.
  * Send email with a photo.
* The second will be a Python server. 
  * Starts a web server with a route called "/check-photos".
  * The route will: 
    * Say how many photos have been taken since last checked.
    * Provide the path to the most recent photo.
* Finally, we will make the program launch on boot.

## Part 1

* PIR Sensor
* Camera
* Write into log file
* Send email with photo
* See s14_project_sensor.py

## Part 2

* Web Server
* Displays number of photos since last visit to /check-photos
* Displays latest photo taken when going to /check-photos
* See s14_project_server.py

## Launch your programs on boot

We use systemd.

1. `cd /lib/systemd/system` 
2. `sudo vi project_take_photos.service`
3. Paste the following:
```
[Unit]
Description=Project Take Photos
After=multi-user.target

[Service]
Type=simple
User=pi
ExecStart=/usr/bin/python3 /home/pi/Desktop/code/s14_project_sensor.py

[Install]
WantedBy=multi-user.target
```
4. Repeat for `sudo vi project_check_photos.service`
5. Paste the following:
```
[Unit]
Description=Project Take Photos
After=multi-user.target

[Service]
Type=simple
User=pi
ExecStart=/usr/bin/python3 /home/pi/Desktop/code/s14_project_server.py

[Install]
WantedBy=multi-user.target
```
6. Run `sudo systemctl enable project_take_photos.service`
7. Run `sudo systemctl enable project_check_photos.service`
8. Run `sudo systemctl start project_take_photos.service`
9. Run `sudo systemctl start project_check_photos.service`
10. Run `sudo systemctl list-units --type=service` to check if they are running.

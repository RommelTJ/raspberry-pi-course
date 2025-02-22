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

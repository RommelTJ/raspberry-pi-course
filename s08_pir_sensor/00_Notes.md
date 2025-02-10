# Detect Movement with a PIR Sensor

Detecting movement with a passive infrared sensor.

Used to turn on lights, for example. Using HC-SR501. The output of the sensor if binary.

## Tune the PIR Sensor

* Before you start, you need to tune the PIR sensor.
* Take out the yellow jumper. Move the jumper to the high position (you can tell the Low position by a small "L").
* Identify the two orange potentiometers. With a screwdriver, turn them. Orient the sensor on the bottom.
  * The first potentiometer controls the range of the sensor. The minimum range is 3m. The maximum range is 7m.
    Turn counter-clockwise to reach the minimum range. Turn clockwise to reach the maximum range. 
    We are leaving it in the middle.
  * The second potentiometer controls the delay of the sensor. How long the sensor will stay high after detecting movement.
    The minimum is 3s. The maximum is 300s (5 minutes). We are leaving it in the minimum.

## Add the PIR sensor to your circuit

* Grab the sensor and a resistor.
* With the PIR sensor facing up, connect the left pin to the ground pin of the breadboard.
* The middle pin of the PIR sensor is the data pin.
* The right pin of the PIR sensor is the power pin.
* Connect the power pin to the 5v pin of the Pi. We used Pin 2.
* Place the resistor on the breadboard.
* Connect the data pin to one side of the resistor.
* Connect the other side of the resistor to GPIO 4 (Pin 7 to the left of the ground).
* You're done!

## Detect movement with Python

* The PIR sensor takes about 1 minute to initialize.
* See s08_01_detect_movement.py

## Automatic Lighting Control

* Turn on the red LED if movement is detected.
* Use `pir.when_motion = my_function` and `pir.when_no_motion = my_function`. 
* See s08_02_automatic_lighting_control.py

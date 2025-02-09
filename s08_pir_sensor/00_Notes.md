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

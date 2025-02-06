# Practice with GPIOs

## Turn on the LED when the button is pressed

* Make the LED power on when the button is pressed, and off when the button is released.
* See 01_ButtonControl2.py
* Then optimize it to use less CPU.
  * We add a sleep to the loop to reduce the CPU usage.
  * Sleep of 0.01 seconds is running at 100 Hz
  * See 01_ButtonControl2_lessCPU.py
* Then optimize it using the library.
  * Using the callback functions and the pause function to wait for the callbacks
  * See 01_ButtonControl3.py

## Add more LEDs to your circuit

* Grab a blue and green LED and two resistors
* Connect them in the same way as the red LED (from the previous exercise)
* Connect them to GPIO 27 (Pin 13) and GPIO 22 (Pin 15)

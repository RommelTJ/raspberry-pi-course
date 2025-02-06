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

## Switch the LED when pressing the button

* Make it so that when the button is pressed, the LED turns on to a different color
  * All lights start off
  * First push is red light on
  * Second push is blue light on
  * Third push is green light on
  * And so on, cycling through the colors
* See 02_ButtonControl.py
* We then added a bounce time to the button to make it easier to press

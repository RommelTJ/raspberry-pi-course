# Control Raspberry Pi's GPIOs with Python

## How GPIOs work

* GPIOs haven't changed from Pi4 to Pi5.
* You can get a list of the Pins by googling "Raspberry Pi GPIO Pinout"
  * https://pinout.xyz/
* Each GPIO has a number. That's the number you use to refer to it in Python.
* How are GPIOs used?
  * Each GPIO can be set to Input or Output. 
  * Only two pins are 5V (pins 2 and 4). These are used for devices that require a high current, such as LED panels, LED strips, or motors.
  * Input: When you want to read some data.
    * Read Data from sensor. High (3.3V) or Low (close to 0V).  
  * Output: When you want to send data to the GPIO.
    * Write data to actuator. High (3.3V) or Low (close to 0V).

## Create a Python program to make an LED blink

* Open Thonny and create a new Python file.
* See 01_BlinkControl.py

## Set the LED's state from user input

* Take the input from the user, 0 or 1.
* If the user enters 0, turn the LED off.
* If the user enters 1, turn the LED on.
* See 02_BlinkControl.py

## Add a Push button to your circuit

* Shut down the Pi.
* Grab a push button and a resistor.
* Connect the push button to the middle of the breadboard.
* Set up a ground wire to the breadboard on the same row as the push button.
* Add a resistor to the other side of the push button.
* Complete the circuit to GPIO 26 (Pin 37; second to last pin on the inside of the Pi).

## Detect when a button is pressed with Python

* See 03_ButtonControl.py

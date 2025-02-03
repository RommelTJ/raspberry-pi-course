# Building your first raspberry pi circuit

## How to safely manipulate your board

- You can't get hurt.
- But you can damage your raspberry pi.
- ALWAYS power off your Pi first if you make a change in the circuit.
- When powered on, avoid touching the circuit. This may cause electrostatic discharge.
- DOUBLE AND TRIPLE CHECK everything before plugging the power cable.
- Start the circuit by connecting the GND (ground) for all components.
- Don't put a 5V signal on a GPIO pin (3.3V max).

## Understand how a Breadboard Works

- Useful for prototyping and testing.
- You can plug in wires, resistors, LEDs, etc.
- Underneath the board, there are wires connecting all components on this line.
- The blue line is the GND (ground) line.
- The red line is the 5V (power) line.
- All the dots are connected to the same line.
- The dots in the middle are connected vertically. That's where you connect the GPIO pins.

## The resistors color code

- A resistor lowers the amount of current that flows thought a component (like an LED).
- They also protect the GPIO pins from being damaged by too much current.
- Which resistor to use?
- They are color coded, with up to 5 bands.
- Don't go below 330 Ohm
- The raspberry pi limit is 50 milliamperes (mA).
- The higher the resistor value, the less current you will take and thus the more LEDs you can connect while keeping your circuit safe.

| - Color - | - Band 1 - | - Band 2 - | - Band 3 - | - Multiplier Band - | - Tolerance Band - |
|-----------|------------|------------|------------|---------------------|--------------------|
| Black     | 0          | 0          | 0          | 1 Ohm               |                    |
| Brown     | 1          | 1          | 1          | 10 Ohm              | +- 1% (F)          |
| Red       | 2          | 2          | 2          | 100 Ohm             | +- 2% (G)          |
| Orange    | 3          | 3          | 3          | 1 kOhm              |                    |
| Yellow    | 4          | 4          | 4          | 10 kOhm             |                    |
| Green     | 5          | 5          | 5          | 100 kOhm            | +- 0.5% (D)        |
| Blue      | 6          | 6          | 6          | 1 M Ohm             | +- 0.25% (C)       |
| Violet    | 7          | 7          | 7          | 10 M Ohm            | +- 0.10% (B)       |
| Grey      | 8          | 8          | 8          |                     | +- 0.05%           |
| White     | 9          | 9          | 9          |                     |                    |
| Gold      |            |            |            | 0.1 Ohm             | +- 5% (J)          |
| Silver    |            |            |            | 0.01 Ohm            | +- 10% (K)         |

Examples: 
- A 4 band resistor. The first 2 bands are brown and black, the middle band is red, the last band is gold.
  - 1 + 0 = 10; 10 * 100 Ohm = 1k Ohm 
- A 5 band resistor. The first 3 bands are brown and black, the middle band is brown, the last band is gold.
  - 1 + 0 + 0 = 100; 100 * 10 Ohm = 1k Ohm

## Building a circuit

* You start with the ground.
* From the Pi pins, count to the fifth pin. That pin is the ground. Connect it to a ground pin on the breadboard.
* By convention, ground is usually connected vi a black wire.
* Then, connect the LED. The short side is the negative side and the long side is the positive side.
* Connect the short side of the LED to the ground on the breadboard.
* Connect the long side of the LED to a resistor to any dot in the middle of the breadboard.
* Finally, to close the circuit, connect the resistor to the GPIO 17 pin on the Pi, (which is to the right of the ground), via a yellow wire.

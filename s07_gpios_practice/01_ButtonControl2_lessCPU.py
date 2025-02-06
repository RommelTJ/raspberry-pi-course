from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(26)

while True:
    # Run at 100 Hz
    sleep(0.01)
    if button.is_pressed:
        led.on()
    else:
        led.off()

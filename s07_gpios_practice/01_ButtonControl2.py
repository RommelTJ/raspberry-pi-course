from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(26)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()

from gpiozero import Button
from time import sleep

button = Button(26)

# print(button.is_pressed)

while True:
    if button.is_pressed:
        print("Button Pressed")
        sleep(1)

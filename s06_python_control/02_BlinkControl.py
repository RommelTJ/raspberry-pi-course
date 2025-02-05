from gpiozero import LED
from time import sleep

led = LED(17)

user_choice_string = input("Please enter 0 to turn off the LED, or 1 to turn on the LED: ")
try:
    choice = int(user_choice_string)
    if choice == 0:
        led.off()
    elif choice == 1:
        led.on()
    else:
        print("Invalid Number")
    sleep(2)
    exit()
except ValueError:
    print("Invalid Number")
    exit()

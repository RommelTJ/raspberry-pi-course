from gpiozero import LED, Button
from signal import pause

button = Button(26, bounce_time=0.05)

red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

lights = [red_led, blue_led, green_led]
led_index = 0

def switch_lights():
    global led_index
    [l.off() for l in lights]
    lights[led_index].on()
    led_index = (led_index + 1) % len(lights)

button.when_pressed = switch_lights
pause()

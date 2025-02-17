from flask import Flask
from gpiozero import Button, LED

app = Flask(__name__)

button = Button(26, bounce_time=0.05)
red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/push-button')
def push_button():
    """Tells you if the button is currently pressed or not"""
    if button.is_pressed:
        return 'Button pressed!'
    return 'Button NOT pressed!'

@app.route('/led/<int:led_number>/state/<int:state>')
def led_state(led_number: int, state: int):
    """Turns the LED on or off"""
    valid_leds = {
        1: red_led,
        2: blue_led,
        3: green_led
    }

    valid_states = {
        0: False,
        1: True
    }

    # First, check if the number is valid. Only 1, 2, and 3 are valid.
    if led_number not in valid_leds:
        return 'Invalid LED number'

    # Next, check if the state is valid. Only 0 and 1 are valid.
    if state not in valid_states:
        return 'Invalid state'

    # Finally, turn the LED on or off.
    led = valid_leds[led_number]
    if state == 1:
        led.on()
    else:
        led.off()
    return f'LED {led_number} is now {"on" if state == 1 else "off"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

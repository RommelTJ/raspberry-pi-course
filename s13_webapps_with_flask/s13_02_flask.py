from flask import Flask
from gpiozero import Button

app = Flask(__name__)
button = Button(26, bounce_time=0.05)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/push-button')
def push_button():
    """Tells you if the button is currently pressed or not"""
    if button.is_pressed:
        return 'Button pressed!'
    return 'Button NOT pressed!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

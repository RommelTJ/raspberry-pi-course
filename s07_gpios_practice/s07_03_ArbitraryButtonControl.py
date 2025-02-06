from gpiozero import LED, Button
from signal import pause
from typing import List

class LightSequencer:
    def __init__(self, light_pins: List[int], button_pin: int = 26):
        self.button = Button(button_pin)
        self.lights = [LED(pin) for pin in light_pins]
        self.current_index = 0
        self.button.when_pressed = self.switch_lights

    def switch_lights(self):
        [light.off() for light in self.lights]
        self.lights[self.current_index].on()
        self.current_index = (self.current_index + 1) % len(self.lights)

    def run(self):
        pause()

if __name__ == '__main__':
    sequencer = LightSequencer(light_pins=[17, 27, 22])
    sequencer.run()

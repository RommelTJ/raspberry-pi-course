from gpiozero import LED, MotionSensor
from signal import pause
from typing import List

class MotionLightControl:
    def __init__(self, light_pins: List[int]):
        self.lights = [LED(pin) for pin in light_pins]
        self.pir_sensor = MotionSensor(4)
        self.pir_sensor.when_motion = self.turn_lights_on
        self.pir_sensor.when_no_motion = self.turn_lights_off

    def turn_lights_on(self):
        [light.on() for light in self.lights]

    def turn_lights_off(self):
        [light.off() for light in self.lights]

    def run(self):
        pause()

if __name__ == '__main__':
    c = MotionLightControl(light_pins=[17, 27, 22])
    c.run()

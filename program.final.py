# Add your Python code here. E.g.
from microbit import *

period = 10
pin16.set_analog_period(period)

while True: 
    knob = pin2.read_analog()
    m = (2.3 - .55) / 1023
    b = .55
    t = m * knob + b
    pin16.write_analog(t / period * 1024)

import time
from machine import Pin,PWM

def fadeLedX(x=1, pinNr=2, freq=20000, stepTime=0.001):
    count=0
    dc=1
    while count < x:
        while dc < 1023:
            pwm = PWM(Pin(pinNr), freq=freq, duty=dc)
            dc += 1
            time.sleep(stepTime)
        while dc > 1:
            pwm = PWM(Pin(pinNr), freq=freq, duty=dc)
            dc -= 1
            time.sleep(stepTime)
        count += 1
    pwm.deinit()

def fadeLedTime(blinkTime=1, pinNr=2, freq=20000, stepTime=0.001):
    count = 0
    x = blinkTime / (stepTime * 2 * 1023)
    dc = 1
    while count < x:
        while dc < 1023:
            pwm = PWM(Pin(pinNr), freq=freq, duty=dc)
            dc += 1
            time.sleep(stepTime)
        while dc > 1:
            pwm = PWM(Pin(pinNr), freq=freq, duty=dc)
            dc -= 1
            time.sleep(stepTime)
        count += 1
    pwm.deinit()

fadeLedX(2,12)

fadeLedTime(5,12)

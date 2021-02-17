from machine import Pin,PWM

pwm = PWM(Pin(12), freq=20000, duty=512)

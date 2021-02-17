# main.py
import socket
import time
from machine import ADC, Pin
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.2.9', 1234))

tempSensor = ADC(Pin(32))
tempSensor.atten(ADC.ATTN_6DB)
tempSensor.width(ADC.WIDTH_10BIT)
led = Pin(12, Pin.OUT)
while True:
    temp = (tempSensor.read()/1024 * 2 - .5)*100
    print(temp)
    s.send(bytes(str(temp),'utf-8'))
    command = s.recv(1024).decode('utf-8')
    print(command)
    if command == 'led_on':
        led.on()
    elif command == 'led_off':
        led.off()
    time.sleep(2)

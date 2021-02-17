# boot.py - - runs on boot-up
import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('H369AE0E094', '1234567890Zaq')
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())
    else:
        print('already connected')
        print('network config:', wlan.ifconfig())


do_connect()

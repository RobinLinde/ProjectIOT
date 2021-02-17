import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    print(f'Connection from {address}')
    while 1:
        temp = float(clientsocket.recv(1024).decode('utf-8'))
        if temp > 20:
            clientsocket.send(bytes('led_on','utf-8'))
        else:
            clientsocket.send(bytes('led_off','utf-8'))
        print(temp)

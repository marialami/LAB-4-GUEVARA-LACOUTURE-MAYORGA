import socket
import random


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


port = 15200
server = get_ip()
address = (server, port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(address)
print("El servidor esta listo para recibir")
print("IP del servidor: "+server)

while True:
    randomNumer = random.randint(0, 10)
    data, clientAddress = serverSocket.recvfrom(4096)
    print(data.decode('utf-8'))
    serverSocket.settimeout(1000)
    msg = bytes("[SERVIDOR]" + data.decode('utf-8'), encoding='utf-8')
    msgmalo = bytes("", encoding='utf-8')
    if randomNumer < 5:
        serverSocket.sendto(msg, clientAddress)

    else:
        serverSocket.sendto(msgmalo, clientAddress)

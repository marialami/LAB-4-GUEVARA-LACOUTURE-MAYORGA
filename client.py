import socket

address = input('Ingrese la IP del servidor: ')
serverName = socket.gethostbyname(socket.gethostname())
port = 15200
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
prefix = "["+socket.gethostname()+"]"
clientSocket.settimeout(1000)

for i in range(10):
    ping = f"ping {i+1}".upper()
    finalMessage = f"[{socket.gethostname()}] {ping} {clientSocket.gettimeout()}ms"
    clientSocket.sendto(finalMessage.encode(),(address,port))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    modifiedFinalMessage = modifiedMessage.decode('utf-8')
    print(modifiedFinalMessage.replace(prefix,""))

clientSocket.close()
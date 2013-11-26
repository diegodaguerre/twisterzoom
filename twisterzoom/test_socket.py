# Echo client program
import socket
import select


HOST = '10.196.71.251'    # The remote host
PORT = 10001              # The same port as used by the server
num = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
entradas = [s]

while num < 50:
    entrada, salida, errores = select.select(entrada, [], [])
	data = s.recv(1024)
	print 'Received', repr(data)
	num = num +1

s.close()

# Echo client program
import socket
import time
import select

HOST = '10.196.71.251'    # The remote host
PORT = 10001              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cmd_open = "open\n"
cmd_time = "time\n"

s.send(cmd_open)

time.sleep(2)

s.send(cmd_time)

num = 0

entrada = [s]

while num < 20:
    entrada, salida, errores = select.select(entrada, [], []) 
    data = s.recv(2048)
    print 'Received', repr(data)
    num = num +1

s.close()

"""
Salida:
Received '\r\nService connection opened (COM0) \r\n\r\n/Ext/MAWS301 W> '
Received 't'
Received 'i'
Received 'me\r\n'
Received 'Time '
Received 'is: Fri N'
Received 'ov 29 15:07:14 201'
Received '3\r\n\r\n/Ext/MAWS301'
Received ' W> '
"""
# Echo client program
import socket
import select


HOST = '10.196.71.251'    # The remote host
PORT = 10001              # The same port as used by the server
num = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
entrada = [s]

while num < 50:
    entrada, salida, errores = select.select(entrada, [], []) 
    data = s.recv(4096)
    print 'Received', repr(data)
    num = num +1

s.close()

"""
Received '\x01WIND\x02\t   4.6\t  130\t\x03\r\n'
Received '\x01WIND\x02\t   4.1\t  122\t\x03\r\n'
Received '\x01WIND\x02\t   5.0\t  131\t\x03\r\n'
Received '\x01WIND\x02\t   6.0\t  125\t\x03\r\n'
Received '\x01WIND\x02\t   4.6\t  125\t\x03\r\n'
Received '\x01WIND\x02\t   4.6\t  142\t\x03\r\n'
Received '\x01WIND\x02\t   4.4\t  133\t\x03\r\n'
Received '\x01WIND\x02\t   5.5\t  133\t\x03\r\n'
Received '\x01WIND\x02\t   4.5\t  130\t\x03\r\n'
Received '\x01WIND\x02\t   4.1\t  120\t\x03\r\n'
Received '\x01PTU\x02\t23.5  \t23.9  \t22.8  \t70  \t75  \t69  \t17.9  \t18.4  \t17.4  \t1'
Received '006.2\t1007.1\t1006.1\t225  \t495  \t142  \t0.0   \t0.0   \t0.0   \t0.0  '
Received ' \t0.0   \t0.0   \t0.0   \t\x03\r\n'
Received '\x01WIND\x02\t   4.1\t  120\t\x03\r\n'
Received '\x01WIND\x02\t   5.3\t  148\t\x03\r\n'
Received '\x01WIND\x02\t   5.3\t  136\t\x03\r\n'
Received '\x01WIND\x02\t   5.0\t  126\t\x03\r\n'
Received '\x01WIND\x02\t   5.7\t  129\t\x03\r\n'
Received '\x01WIND\x02\t   5.0\t  133\t\x03\r\n'

"""
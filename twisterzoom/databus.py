"""
Data bus handler

"""

import socket
import logging


logger = logging.getLogger('tz.databus')


class DataBus(object):

    def __init__(self, uri):
        family, type, address = parse_socket_uri(uri, defaultport=9921)
        self._socket = socket.socket(family, type)
        self._errno = self._socket.connect_ex(address)

    def fileno(self):
        return self._socket.fileno()

    def recv(self):
        # do something

    def send(self, msg):
        # do something

    def close(self):
        if self._errno == 0:
            self._socket.close()
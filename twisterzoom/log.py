import logging
from logging.handlers import SysLogHandler, DatagramHandler

LOGFORMAT = '%(relativeCreated)10.2f %(levelname)7s:%(name)-15s %(message)s'
LOGDATEFMT = '%Y%m%d %H:%M:%S'
def start_logging(dsts='console', level='DEBUG'):
    if isinstance(dsts, basestring):
        dsts = dsts.split(',')

    level = getattr(logging, level.upper())
    root = logging.getLogger()
    root.setLevel(logging.NOTSET)
    formatter = logging.Formatter(LOGFORMAT, LOGDATEFMT)

    for dst in dsts:
        if dst == 'console':
            hdlr = logging.StreamHandler()
        elif dst == 'syslog':
            hdlr = SysLogHandler('/dev/log')
        elif dst.startswith('udp'):
            parts = dst.split(':')
            host, port = '127.0.0.1', 9922
            if len(parts) == 3:
                host, port = parts[1:3]
            elif len(parts) == 2:
                host = parts[1]
            hdlr = DatagramHandler(host, int(port))
        else:
            hdlr = logging.FileHandler(dst, 'a')

        hdlr.setLevel(level)
        hdlr.setFormatter(formatter)
        root.addHandler(hdlr)

    return root

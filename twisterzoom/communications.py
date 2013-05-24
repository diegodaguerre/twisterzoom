"""
doc

"""
import select
import logging
from twisterzoom.databus import DataBus


logger = logging.getLogger('tz.comm')


class Communications(object):

    def __init__(self, systembus, databusuri):
        self._cycle = True
        self._systembus = systembus
        self._databus = DataBus(databusuri)
        self._rmap = {
            self._systembus: self._read_systembus,
            self._databus: self._read_databus,
        }

    def stop(self):
        self._cycle = False

    def start(self):
        try:
            while self._cycle:
                rlist, _, _ = select.select(self._rmap.keys(), [], [], 0.5)
                for r in rlist:
                    self._rmap[r]()
        finally:
            for bus in self._rmap:
                bus.close()

    def _route(self, msgs):
||||||||pass
        # do something

    def _read_systembus(self):
        msg = self._systembus.recv()
        self._route([msg])

    def _read_databus(self):
        msgs = self._databus.recv()
        self._route(msgs)
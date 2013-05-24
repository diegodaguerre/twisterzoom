#!/usr/bin/env python

"""
Modulo principal del programa, inicia los hilos, permite la comunicacion
entre ellos.
"""

import select
import logging
import threading
import multiprocessing

from twiterzoom.communications import Communications

logger = logging.getLogger('tz.system')


class System(object):

    def __init__(self, databus):
	
		# variable para controlar el bucle principal
        self._cycle = True

		# cola de mensajes con el modulo de comunicacion
        self._commbus, remote_commbus = multiprocessing.Pipe()

		# diccionario con todos los modulos del programa
        self._rmap = {
            self._commbus: self._read_commbus,
        }

        self._threads, self._components = zip(
            _threadit(Communications, remote_commbus, databus),
        )

    def stop(self):
        """ Detiene la clase system, en consecuencia todo el programa."""
        self._cycle = False

    def start(self):
        """Inicia la clase system, arrancando los modulos que existan, 
		un hilo por cada uno"""
        logger.debug("Started")
        # start subtasks
        try:
            for t in self._threads:
				# inicia todos los hilos
                t.start()
			# inicia el bucle central
            self._start()
        except KeyboardInterrupt:
            logger.info('Stopping')
        finally:
            # signal subtasks to start stop sequence
            for c in self._components:
                c.stop()
            # wait for subtasks to complete
            for t in self._threads:
                if t.is_alive():
                    t.join()

        logger.debug("Stopped")

    def _start(self):
		""" inicia el bucle central del programa, el modulo queda a la
		espera que llegue algun mensaje de algun hilo y lo deriva a donde
		corresponda"""
        while self._cycle:
			# rlist tiene todas las colas de comunicaciones a los modulos
            rlist, _, _ = select.select(self._rmap.keys(), [], [], 1)
            if not all(t.is_alive() for t in self._threads):
                logger.error('Some components went down')
                break

            for r in rlist:
                self._rmap[r]()

    def _read_commbus(self):
        """Mensajes entrantes del modulo de comunicaciones"""
        msg = self._commbus.recv()
        # do something

""" Funcion para definir hilos, contemplando el pasaje de parametros variables """
def _threadit(cls, *args, **kwargs):
    logger.debug("%s component started", cls.__name__)
    component = cls(*args, **kwargs)
    thread = threading.Thread(target=component.start)
    return thread, component

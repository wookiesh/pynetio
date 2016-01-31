"""
inding library for Koukaam netio devices
"""

import time
import socket
import logging
from telnetlib import Telnet
from threading import Lock

LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-instance-attributes
class Netio(object):
    """ Simple class to handle Telnet communication with the Netio's """

    MAX_RETRIES = 2

    def __init__(self, host, port, username, password):
        """ Let's initialize """
        self.host, self.port = host, port
        self.username, self.password = username, password
        self.states = [False] * 4
        self.consumptions = [0] * 4
        self.cumulated_consumptions = [0] * 4
        self.start_dates = [""] * 4
        self.retries = self.MAX_RETRIES
        self.telnet = None
        self.lock = Lock()
        self.connect()

    def connect(self):
        """ Simple connect """
        try:
            self.telnet = Telnet(self.host, self.port)
            time.sleep(1)
            self.get()
            self.get('login admin admin')
            self.update()
        except socket.gaierror:
            LOGGER.error("Cannot connect to %s (%d)",
                         self.host, self.retries)

    def update(self):
        """ Update all the switch values """

        self.states = [bool(int(x)) for x in self.get('port list') or '0000']

    # def keep_alive(self):
    #     self.get('version')

    def get(self, command=None):
        """
        Interface function to send and receive decoded bytes
        Retries the connect [self.retries] times

        """

        try:
            assert self.telnet
            with self.lock:
                if command:
                    if not command.endswith('\r\n'):
                        command += '\r\n'
                    LOGGER.debug('%s: sending %r', self.host, command)
                    self.telnet.write(command.encode())

                res = self.telnet.read_until('\r\n'.encode()).decode()
                LOGGER.debug('%s: received %r', self.host, res)
                if res.split()[0] not in ('100', '250'):
                    LOGGER.warn('command error: %r', res)
                return res.split()[1]

        except (EOFError, socket.gaierror):
            LOGGER.error("Cannot get answer from %s (%d)",
                         self.host, self.retries)
            if self.retries > 0:
                self.retries -= 1
                self.connect()
                return self.get(command)
            else:
                self.retries = Netio.MAX_RETRIES
                return None

    def stop(self):
        """ Close the telnet connection """
        self.telnet.close()

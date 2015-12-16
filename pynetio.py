import time
import socket
import logging
from telnetlib import Telnet
from threading import Lock


class Netio(object):
    MAX_RETRIES = 2

    """ Simple class to handle Telnet communication with the Netio's """

    def __init__(self, host, port, username, password):
        """ Let's initialize """
        self.host, self.port = host, port
        self.log = logging.getLogger(__name__)
        self.username, self.password = username, password
        self._states = []
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
            self.log.error("Cannot connect to %s (%d)" %
                           (self.host, self.retries))

    @property
    def states(self):
        """ Get the states """
        return self._states

    def update(self):
        """ Update all the switch values """

        self._states = [bool(int(x)) for x in self.get('port list') or '0000']

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
                    self.log.debug('%s: sending %r' % (self.host, command))
                    self.telnet.write(command.encode())

                res = self.telnet.read_until('\r\n'.encode()).decode()
                self.log.debug('%s: received %r' % (self.host, res))
                if res.split()[0] not in ('100', '250'):
                    self.log.warn('command error: %r' % res)
                return res.split()[1]

        except Exception:
            self.log.error("Cannot get answer from %s (%d)" %
                           (self.host, self.retries))
            if self.retries > 0:
                self.retries -= 1
                self.connect()
                return self.get(command)
            else:
                self.retries = self.MAX_RETRIES
                return None

    def stop(self):
        """ Close the telnet connection """
        self.telnet.close()

# Not really a unit test yet, but functional..
# Pass hostname, port, username and password as arguments of testing..

import sys
import pynetio
import logging

logging.basicConfig(level=logging.DEBUG)

dev = pynetio.Netio(*sys.argv[1:])
print(dev.states)

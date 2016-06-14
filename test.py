# -*- coding: utf-8 -*-

# Not really a unit test yet, but functional..
# Pass hostname, port, username and password as arguments of testing..

import sys
import logging
import pynetio

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    dev = pynetio.Netio(*sys.argv[1:])
    print dev.states

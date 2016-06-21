#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

from spyne.application import Application
from spyne.util.wsgi_wrapper import WsgiMounter
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from Sonos_Soap import Sonos

app = Application([Sonos],
    tns='http://www.sonos.com/Services/1.1',
    in_protocol=Soap11(),
    out_protocol=Soap11(cleanup_namespaces=True)
)


if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(app)
    server = make_server('0.0.0.0', 7789, wsgi_app)
    server.serve_forever()

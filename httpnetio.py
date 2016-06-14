# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, **params):
        print (params)
        self.write('ok')

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/states', MainHandler),
    ])
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

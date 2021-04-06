
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class zhendong(tornado.web.RequestHandler):
    def get(self):
        self.render("zhendong.html")

class stop(tornado.web.RequestHandler):
    def get(self):
        tornado.ioloop.IOLoop.current().stop()


class index_page(tornado.web.RequestHandler):
    def get(self):
        self.render("index_page.html")




class power_lot(tornado.web.RequestHandler):
    def get(self):
        self.render("power.html")



class duifeng(tornado.web.RequestHandler):
    def get(self):
        self.render("duifeng.html")
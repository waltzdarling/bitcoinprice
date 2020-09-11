import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers['Content-Type'] == 'application/json':
            self.args = json.loads(self.request.body)

    def post(self):
        self.write(f"Hello, from Veronika. Your email is: {self.args.email}. Your preference price is {self.args.price}")


def make_app():
    return tornado.web.Application([
        (r"/hello", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
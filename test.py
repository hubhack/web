# import socketserver
# class Handler(socketserver.BaseRequestHandler):
#     def Handle(self):
#         super().handle()
#         r = self.request
#         data = r.recv(1024)
#         print(data)
#
#
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9999))
# server.serve_forever()

from wsgiref.simple_server import make_server
def demo_app(environ, start_response):
    status = "200 ok"
    headers = [('Content-Type','text/html; charset=utf-8')]

    start_response(status, headers)
    html = '<h1>哈哈</h1>'.encode("utf-8")
    return [html]


ws = make_server('127.0.0.1',9999, demo_app)
ws.serve_forever()

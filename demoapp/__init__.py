#!/usr/bin/env python
import http.server

RESPONSE='''Hi there!'''

class myHandlers(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(RESPONSE, 'UTF-8'))

def run(server_class=http.server.HTTPServer, handler_class=myHandlers):
    server_address = ('', 8000)
    myserver = server_class(server_address, handler_class)
    myserver.serve_forever()

if __name__ == "__main__":
    run()

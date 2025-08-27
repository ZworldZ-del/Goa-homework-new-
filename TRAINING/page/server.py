import http.server
import socketserver

PORT = 80 


DIRECTORY = "index.html"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://Warn.system:{PORT}/")
    httpd.serve_forever()

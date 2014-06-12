import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

handler_class = SimpleHTTPRequestHandler
server_class = BaseHTTPServer.HTTPServer
protocol = "HTTP/1.0"

if sys.argv[1:]:
	port = int(sys.argv[1])
else:
	port = 8000
server_address = ('0.0.0.0', port)

handler_class.protocol_version = protocol
http = server_class(server_address, handler_class)

sa = http.socket.getsockname()
print "Starting HTTP on", sa[0], "on port", sa[1], '.'
http.serve_forever()
from http.server import *

class Handler(BaseHTTPRequestHandler):
	def handle_one_request(self):
		self.command = "GET"
		return BaseHTTPRequestHandler.handle_one_request(self)
	def do_GET(self):
		"""NEVER errors out! Reliability is key! The same things we've come
		to expect from mature web platforms like PHP!"""
		self.send_response(204)
		self.end_headers()

httpd = HTTPServer(('', 8000), Handler)
httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import configparser

config = configparser.ConfigParser()
config.read('properties/config.properties')

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello World')
        elif self.path.startswith('/hello/'):
            if len(path_parts) == 2:
                name = path_parts[1]
                message = f"Hello {name}".encode()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(message)
        elif self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status": "OK"}')
        else:
            self.send_error(404, "File not found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = (config['DEFAULT']['APP_HOST'], int(config['DEFAULT']['PORT']))
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on {server_address[0]}:{server_address[1]}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

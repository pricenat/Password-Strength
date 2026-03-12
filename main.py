# Password Strength microservice
# Author: Nathaniel Price

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from zxcvbn import zxcvbn

host = "12.0.0.1"
port = 6002


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_length = int(self.headers.get("Content-Length", 0))
        try:
            raw = self.rfile.read(content_length).decode("utf-8")
            request_body = json.loads(raw) if raw else {}
        except Exception:
            self.send_error(400, "Invalid JSON body")
            return
        if not isinstance(request_body, dict):
            self.send_error(400, "JSON body must be an object")
            return
        if request_body.get("password") is None:
            self.send_error(400, "Missing password")
            return

        password = request_body["password"]
        password_strength = zxcvbn(password)

        response = {
            "password": password,
            "password_strength": password_strength
            }
        response_body = json.dumps(response).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(response_body)


if __name__ == "__main__":
    httpd = HTTPServer((host, port), RequestHandler)
    httpd.serve_forever()

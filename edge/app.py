import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

class Handler(BaseHTTPRequestHandler):
    def reply(self, status, text):
        data = text.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            return self.reply(200, "ok\n")
        if parsed.path != "/check":
            return self.reply(404, "not found\n")
        host = parse_qs(parsed.query).get("host", [""])[0]
        if not host:
            return self.reply(400, "missing host\n")
        # Intentional medium-level foothold: diagnostic input reaches a shell.
        result = subprocess.run(f"ping -c 1 -W 1 {host}", shell=True,
                                capture_output=True, text=True)
        self.reply(200, result.stdout + result.stderr)

    def log_message(self, *_args):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

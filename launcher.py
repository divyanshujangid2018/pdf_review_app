"""Entry point for the standalone app build: starts the server on a free
local port, opens it in the default browser, and shows a menu-bar icon
with an "Open" and "Quit" item so the app has a visible way to stop."""
import socket
import threading
import time
import urllib.request
import webbrowser

import rumps
import uvicorn

from app import app


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def open_once_ready(url: str, timeout: float = 10.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            urllib.request.urlopen(url + "/api/health", timeout=0.5)
            webbrowser.open(url)
            return
        except Exception:
            time.sleep(0.2)


class PDFCompareApp(rumps.App):
    def __init__(self, url: str):
        super().__init__("PDF Compare", quit_button="Quit")
        self.url = url
        self.menu = ["Open PDF Compare"]

    @rumps.clicked("Open PDF Compare")
    def open_app(self, _):
        webbrowser.open(self.url)


def main() -> None:
    port = find_free_port()
    url = f"http://127.0.0.1:{port}"

    server = threading.Thread(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": "127.0.0.1", "port": port, "log_level": "warning"},
        daemon=True,
    )
    server.start()
    threading.Thread(target=open_once_ready, args=(url,), daemon=True).start()
    PDFCompareApp(url).run()


if __name__ == "__main__":
    main()

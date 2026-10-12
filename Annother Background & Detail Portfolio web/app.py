"""
Portofolio I G.N.K. Sukma Kertha Dinata
Jalankan:  python app.py
Lalu buka: http://localhost:8000  (otomatis terbuka di browser)

Tidak perlu install library apa pun (hanya Python 3.8+).
Struktur folder:
    app.py
    index.html
    static/   (semua foto, poster, sertifikat, dan CV_Sukma_Kertha_Dinata.pdf)
"""
import http.server
import os
import socketserver
import threading
import webbrowser

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Matikan cache agar perubahan di index.html langsung terlihat saat refresh
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # terminal tetap bersih


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    url = f"http://localhost:{PORT}/index.html"
    with Server(("", PORT), Handler) as httpd:
        print(f"Portofolio berjalan di {url}")
        print("Tekan Ctrl+C untuk berhenti.")
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")

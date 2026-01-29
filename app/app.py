from flask import Flask
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return f"Hello DevOps! Served from host: {socket.gethostname()}\n"

@app.get("/health")
def health():
    return {"status": "ok"}

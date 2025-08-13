from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow React frontend

@app.route("/")
def index():
    return render_template("index.html")  # Flask HTML chat

@socketio.on("send_message")
def handle_send_message(data):
    print("📩 Received message:", data)
    # Broadcast to all connected clients (Flask + React)
    socketio.emit("receive_message", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

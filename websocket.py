from flask_socketio import SocketIO, emit

# Create the SocketIO object
socketio = SocketIO()

# Console log on a connection from a client, kept for debugging purpose
@socketio.on("connect")
def handle_connect():
    print("Client connected")

# Console log on a disconnection from a client, kept for debugging purpose
@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

# Emit an event signaling a new note has been created
def emit_note_added(note):
    socketio.emit("note_added", note)
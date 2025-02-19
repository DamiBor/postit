from flask_socketio import SocketIO, emit
from db import add_note

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

# Event to create a new note in the DB
@socketio.on("create_note")
def create_note(msg):
    print("Note creation requested with text : " + msg)
    add_note(msg)
    emit_note_added(msg)

# Emit an event signaling a new note has been created
def emit_note_added(note):
    emit("note_added", note, broadcast=True)
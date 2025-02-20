import asyncio
from flask import Flask, render_template, request
from db import get_db_connection, get_all_notes
from websocket import socketio
from twitch import init_twitch_chat

# Flask application and socketio server creation
app = Flask(__name__)
socketio.init_app(app)

# Route for the index page of the app
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    # Init and start twitch chat bot with code in url params
    if "code" in request.args:
        asyncio.run(init_twitch_chat(request.args["code"]))

    # Get all existing notes in db and render index.html with them as param
    conn = get_db_connection()
    notes = get_all_notes()
    return render_template('index.html', notes=notes)

# Run the flask app if this file is executed as main
if __name__ == "__main__":
    socketio.run(app, debug=True)


import asyncio
from flask import Flask, render_template, request
from db import get_db_connection, get_all_notes
from websocket import socketio
from twitch import init_twitch_chat
from config import AUTH_TYPE, AuthType

# Flask application and socketio server creation
app = Flask(__name__)
socketio.init_app(app)

# For Server-side authencation, launch auth process now
if AUTH_TYPE == AuthType.SERVER:
    asyncio.run(init_twitch_chat())

# Route for the root page of the app : in case of client-side authentication render login.html, else render directly index without parameters
@app.route('/')
def login():
    if AUTH_TYPE == AuthType.CLIENT:
        return render_template('login.html')
    else:
        return index()

@app.route('/index')
def index():
    # In case of client-side authentication init twitch chat bot with code in url params and render index
    if AUTH_TYPE == AuthType.CLIENT and "code" in request.args:
        asyncio.run(init_twitch_chat(request.args["code"]))

    # Get all existing notes in db and render index.html with them as param
    conn = get_db_connection()
    notes = get_all_notes()
    return render_template('index.html', notes=notes)

# Run the flask app if this file is executed as main
if __name__ == "__main__":
    socketio.run(app, debug=True)

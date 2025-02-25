import asyncio
import argparse
from flask import Flask, render_template, request
from db import get_all_notes, init_db
from websocket import socketio
from twitch import TwitchChatBot
from config import AUTH_TYPE, AuthType, NOTES_VISIBILITY, NOTES_DISPLAY_TIME


# Handle command line options
parser = argparse.ArgumentParser()
parser.add_argument("-fdb", "--ForceInitDB", help = "Force the reinitatialisation of the database, clering the previous content.", action='store_true')
args = parser.parse_args()

# Database initialization
init_db(args.ForceInitDB)

# Flask application and socketio server creation
app = Flask(__name__)
socketio.init_app(app)
chatbot = TwitchChatBot()

# For Server-side authencation, launch auth process now
if AUTH_TYPE == AuthType.SERVER:
    asyncio.run(chatbot.init_twitch_chat())

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
        asyncio.run(chatbot.init_twitch_chat(request.args["code"]))

    # Get all existing notes in db and render index.html with them as param
    notes = get_all_notes()
    return render_template('index.html', notes=notes, notes_vis=NOTES_VISIBILITY, notes_disp_time=NOTES_DISPLAY_TIME)

# Run the flask app if this file is executed as main
if __name__ == "__main__":
    socketio.run(app, debug=False)
    asyncio.run(chatbot.close_twitch_chat())

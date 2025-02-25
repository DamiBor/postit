from enum import Enum
import os

# Authentication type : 
# - CLIENT : ask authentication to the client when it access the root page
# - SERVER : ask authentication upon server starts
class AuthType(Enum):
    CLIENT = 1
    SERVER = 2

AUTH_TYPE = AuthType.SERVER

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
DB_FILE = os.path.join(basedir, 'database.db')

# Notes visibility on frontend :
# * visible : notes will be always visible
# * hidden, notes will be initially hidden, then displayed only when a new one is added for the duration of NOTES_DISPLAY_TIME (in ms)
NOTES_VISIBILITY = "visible"
NOTES_DISPLAY_TIME = 3000
from enum import Enum

# Authentication type : 
# - CLIENT : ask authentication to the client when it access the root page
# - SERVER : ask authentication upon server starts
class AuthType(Enum):
    CLIENT = 1
    SERVER = 2

AUTH_TYPE = AuthType.SERVER
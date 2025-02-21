from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.chat import Chat, EventData, ChatMessage
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.helper import first
from config import AUTH_TYPE, AuthType
from db import add_note

MY_URL = "http://localhost:17563"

class TwitchChatBot():

    def __init__(self):
        self.twitch = Twitch('6q2as8ylmy8g56yp7wvnak1bv7315x', "26w7b3hxdgi6y4zmjg24x30qt1iniq")
        self.chat = None
        self.target_scope = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
        self.target_channel = ""
    
    async def init_twitch_chat(self, code=None):
        # Get token and refresh token from user code, and set authentification with them
        if AUTH_TYPE == AuthType.SERVER:
            auth = UserAuthenticator(self.twitch, self.target_scope, force_verify=False)
            token, refresh_token = await auth.authenticate()
        else:
            auth = UserAuthenticator(self.twitch, self.target_scope, url=MY_URL)
            token, refresh_token = await auth.authenticate(user_token=code)

        await self.twitch.set_user_authentication(token, self.target_scope, refresh_token)

        # Get the user linked to the token : we will acces their chat
        username = await first(self.twitch.get_users())
        self.target_channel = username.display_name

        # Create the chatbox instance and start it
        self.chat = await Chat(self.twitch)
        self.chat.register_event(ChatEvent.READY, self.on_ready)
        self.chat.register_event(ChatEvent.MESSAGE, self.on_message)
        self.chat.start()

    async def close_twitch_chat(self):
        if self.chat != None:
            self.chat.stop()
        await self.twitch.close()

    async def on_ready(self, ready_event: EventData):
        print('Bot is ready for work, joining channel ' + self.target_channel)
        await ready_event.chat.join_room(self.target_channel)

    async def on_message(self, msg: ChatMessage):
        # print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
        if msg.text.startswith("!postit "):
            print(f"Postit cmd :{msg.text}")
            new_note = msg.text.removeprefix("!postit ")
            print(f"New note :{new_note}")
            add_note(new_note)
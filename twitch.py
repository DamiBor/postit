import asyncio
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.helper import first
from twitchAPI.chat import Chat, EventData, ChatMessage
from db import add_note
from config import AUTH_TYPE, AuthType

MY_URL = "http://localhost:17563"
target_channel = ""
target_scope = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]

async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channel ' + target_channel)
    await ready_event.chat.join_room(target_channel)

async def on_message(msg: ChatMessage):
    # print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
    if msg.text.startswith("!postit "):
        print(f"Postit cmd :{msg.text}")
        new_note = msg.text.removeprefix("!postit ")
        print(f"New note :{new_note}")
        add_note(new_note)

async def init_twitch_chat(code=None):
    # Create and init Twitch object instance
    tw = await Twitch('6q2as8ylmy8g56yp7wvnak1bv7315x', "26w7b3hxdgi6y4zmjg24x30qt1iniq")
    # Get token and refresh token from user code, and set authentification with them
    if AUTH_TYPE == AuthType.SERVER:
        auth = UserAuthenticator(tw, target_scope, force_verify=False)
        token, refresh_token = await auth.authenticate()
    else:
        auth = UserAuthenticator(tw, target_scope, url=MY_URL)
        token, refresh_token = await auth.authenticate(user_token=code)

    await tw.set_user_authentication(token, target_scope, refresh_token)

    # Get the user linked to the token : we will acces their chat
    username = await first(tw.get_users())
    global target_channel
    target_channel = username.display_name

    # Create the chatbox instance and start it
    chat = await Chat(tw)
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.start()

    # chat.stop()
    # await tw.close()

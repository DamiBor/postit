# postit
App for managing post-its for streamers on Twitch

Summary : 
This application allows viewers in a Twitch chat room to add textual notes to the streamer displayed as post-its.

How does it work : 
For now, the app works only when executed locally by the streamer.
On start, the app will prompt a Twitch login page then a Twitch authorization request for chat reading and writing for this app using the default web browser. Once accepted, it will display a web page that can be closed. From this moment, the application will be connected to the chat room and will read all messages posted in it.
IMPORTANT : the app will only join the chat room of the user that gave the authorization, so it shall be done with the streamer's account.
The application will ignore all messages in the chat except those beginning with the command !postit. In these messages, the whole text found after !postit is added as a new note in the database.
To display the notes, open a web page on http://localhost:5000/index.

About notes visibility : 
Notes visibility on the index page can be parametered using NOTES_VISIBILITY and NOTES_DISPLAY_TIME in config.py.
If NOTES_VISIBILITY is set to "visible", the notes will be alway displayed.
If NOTES_VISIBILITY is set to hidden, the notes will be initially hidden, only to be displayed when a new one is created. in this case, the notes will be hidden again after the time defined by NOTES_DISPLAY_TIME (in milliseconds).

How to use it : 
Install the app directory wherever you want on your computer. Then open a command prompt in this directory, execute python run.py, and the application is up. It will open a web browser for Twitch authentication, be sure to login with your streamer account so the app join the right chat room.
To display the note on your stream layout, just add a web browser source on the address http://localhost:5000/index.

CREDITS : 
* Twitch authentification Javascript code taken from this blog article (with very few modifications) : https://blog.flozz.fr/2021/01/23/decouverte-des-apis-twitch-2-authentification/
* Twitch Python code on server side strongly inspired from different tutorials on twitchAPI documentation : https://pytwitchapi.dev
# yt_playlist_crawler

A simple and interactive command-line tool for Linux/Mac/Win to fetch your YouTube playlist content into a file.
So you can e.g. save your music discoveries before they will be deleted.

## Quickstart

The code is written in Python3.6. So ensure Python3 is correctly installed.

Install required Python packages via pip3.

`pip3 install -r requirements.txt`

You need to add an API key and OAuth 2.0 token from GoogleAPIs. Paste your API key in `./credentials/api_key.txt` and move the JSON file for the OAuth 2.0 token in `credentials/`. More info: <https://developers.google.com/youtube/v3/docs/>


Then launch the program together with your channel ID. The channel ID begins with 'UC' and is e.g. located in your channel URL.

`python3 main.py --channelID UC_x5XG1OV2P6uZZ5FSM9Ttw`

Then navigate through the menu and choose your desired playlists.


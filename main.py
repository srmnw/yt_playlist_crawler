#! /usr/bin/env python3

"""
Author:     Alexander Sarmanow
Email:      alexander.sarmanow@mailbox.tu-dresden.de
"""
import argparse
import os

import interface
import api
import key_handle
import doc


parser = argparse.ArgumentParser(description='Paste your Channel ID')
parser.add_argument('--channelID', help='Paste your Channel ID')

CREDENTIALS_DIR = 'credentials'


logo = " ===========================================================================\n"
logo += "|                                                                           |\n"
logo += "| ************************       YouTube     ************************       |\n"
logo += "| ************************       Playlist    ************************       |\n"
logo += "| ************************       Crawler     ************************       |\n"
logo += "|                                                                           |\n"
logo += "|                                                                           |\n"
logo += " ===========================================================================\n"


if __name__ == '__main__':
    print(logo)
    args = parser.parse_args()
    channel_id = args.channelID

    if not os.path.exists(CREDENTIALS_DIR):
        os.makedirs(CREDENTIALS_DIR)

    playlists = list()

    private = interface.answer_private_public()
    if 'private' in private:
        api_key = key_handle.get_api_file()
        api_o = api.PrivateAPI(api_key)
    else:
        api_key = key_handle.get_api_key()
        api_o = api.PublicAPI(api_key)
    fetch_all = interface.answer_all()
    if 'fetch all playlists' in fetch_all:
        if 'private' in private:
            playlist_list = api_o.private_pl_list()
        else:
            playlist_list = api_o.public_pl_list(channel_id=channel_id)
    else:
        if 'private' in private:
            playlist_list = api_o.private_pl_list()
        else:
            playlist_list = api_o.public_pl_list(channel_id=channel_id)
        playlist_choose = interface.answer_choose_playlist(playlist_list)
        playlist_list = [item for item in playlist_list if item['snippet']['title'] in playlist_choose]
    for pl in playlist_list:
        if 'private' in private:
            pl_content = api_o.private_playlist(pl['id'])
            doc.create_doc(pl['snippet']['title'], pl_content)
        else:
            pl_content = api_o.public_playlist(pl['id'])
            doc.create_doc(pl['snippet']['title'], pl_content)
    print("===> {} Playlists successful fetched.".format(len(playlist_list)))
    print("Playlists fetching finished.")

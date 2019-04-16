#! /usr/bin/env python3

"""
Author:     Alexander Sarmanow
Email:      alexander.sarmanow@mailbox.tu-dresden.de
"""
import argparse

import interface
import api
import key_handle
import doc


parser = argparse.ArgumentParser(description='Paste your Channel ID')
parser.add_argument('--channelID', help='Paste your Channel ID')

def main():
    pass


if __name__ == '__main__':
    args = parser.parse_args()
    channel_id = args.channelID
    private = interface.answer_private_public()
    if private:
        api_key = key_handle.get_api_file()
    else:
        api_key = key_handle.get_api_key()
    fetch_all = interface.answer_all()
    if fetch_all:
        pass
    else:
        if private:
            playlist_list = api.api_private(api_key)
        else:
            playlist_list = api.api_public(api_key,channel_id=channel_id)
        playlist_list = interface.answer_choose_playlist(api)
    main()
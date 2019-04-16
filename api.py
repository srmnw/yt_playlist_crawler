import os
import json

import googleapiclient.discovery
import google_auth_oauthlib.flow
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def api_public(developer_key, channel_id):
    playlist_list = dict()

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = developer_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId=channel_id,
        maxResults=25
    )
    response = request.execute()
    #response = json.dumps(response, indent=4, sort_keys=True)
    return response["items"]

def api_private(secret_file_path):

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = secret_file_path

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlists().list(
        part="snippet,contentDetails",
        maxResults=25,
        mine=True
    )
    response = request.execute()
    response = json.dumps(response, indent=4, sort_keys=True)
    return response["items"]

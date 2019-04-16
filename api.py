import os
import json

import googleapiclient.discovery
import google_auth_oauthlib.flow
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


class PrivateAPI:
    def __init__(self, secret_file_path):
        self.secret_file_path = secret_file_path

        api_service_name = "youtube"
        api_version = "v3"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            self.secret_file_path, scopes)
        credentials = flow.run_console()
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

    def private_pl_list(self):
        return_obj = list()
        request = self.youtube.playlists().list(
            part="snippet,contentDetails",
            maxResults=50,
            mine=True
        )
        while request is not None:
            response = request.execute()
            for item in response["items"]:
                return_obj.append(item)
            request = self.youtube.playlists().list_next(request, response)
        return return_obj

    def private_playlist(self, playlist_id):
        return_obj = list()

        request = self.youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=playlist_id
        )
        while request is not None:
            response = request.execute()
            for item in response["items"]:
                return_obj.append(item)
            request = self.youtube.playlistItems().list_next(request, response)
        return return_obj


class PublicAPI:
    def __init__(self, developer_key):
        self.developer_key = developer_key

    def public_pl_list(self, channel_id):
        return_obj = list()

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = self.developer_key

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId=channel_id,
            maxResults=50
        )
        while request is not None:
            response = request.execute()
            for item in response["items"]:
                return_obj.append(item)
            request = youtube.playlists().list_next(request, response)
        return return_obj

    def public_playlist(self, playlist_id):
        return_obj = list()
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = self.developer_key

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=playlist_id
        )
        while request is not None:
            response = request.execute()
            for item in response["items"]:
                return_obj.append(item)
            request = youtube.playlists().list_next(request, response)
        return return_obj




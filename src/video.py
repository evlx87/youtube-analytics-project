import os
from googleapiclient.discovery import build


api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id: str):
        self.video_id = video_id
        try:
            video_response = youtube.videos().list(id=self.video_id,
                                                   part='snippet,statistics,contentDetails,topicDetails').execute()
            self.url = 'https://youtu.be/' + video_id
            self.title = video_response['items'][0]['snippet']['title']
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.like_count = None
            self.view_count = None

    def __str__(self):
        return self.title


class PLVideo:
    def __init__(self, video_id: str, playlist_id: str):
        self.__video_id = video_id  # id видео;
        video_response = youtube.videos().list(id=self.__video_id,
                                               part='snippet,statistics,contentDetails,topicDetails').execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.url = 'https://youtu.be/' + playlist_id + '/' + video_id
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.count_likes = video_response['items'][0]['statistics']['likeCount']
        self.__playlist_id = playlist_id

    def __str__(self):
        return self.video_title

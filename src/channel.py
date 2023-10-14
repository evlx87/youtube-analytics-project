import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API.
        """
        self.channel_id = channel_id

        channel = youtube.channels().list(
            id=self.channel_id,
            part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + channel['items'][0]['snippet']['customUrl']
        self.subs_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return f'{int(self.subs_count) + int(other.subs_count)}'

    def __sub__(self, other):
        return f'{int(self.subs_count) - int(other.subs_count)}'

    def __gt__(self, other):
        if int(self.subs_count) > int(other.subs_count):
            return True
        else:
            return False

    def __ge__(self, other):
        if int(self.subs_count) >= int(other.subs_count):
            return True
        else:
            return False

    def __lt__(self, other):
        if int(self.subs_count) < int(other.subs_count):
            return True
        else:
            return False

    def __le__(self, other):
        if int(self.subs_count) <= int(other.subs_count):
            return True
        else:
            return False

    def __eq__(self, other):
        if int(self.subs_count) == int(other.subs_count):
            return True
        else:
            return False

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file):
        with open(file, 'wt') as file:
            data = {'chanel_id': self.channel_id,
                    'title': self.title,
                    'description': self.description,
                    'url': self.url,
                    'subscribers_count': self.subs_count,
                    'video_count': self.video_count,
                    'view_count': self.view_count}
            json_data = json.dumps(data, ensure_ascii=False, indent=2)
            file.write(json_data)

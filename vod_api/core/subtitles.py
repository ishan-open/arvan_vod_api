class SubtitleDataCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response['id']
        self.video_id = response['video_id']
        self.lang = response['lang']
        self.url = response['url']

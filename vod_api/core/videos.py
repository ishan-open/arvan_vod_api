from .channels import ChannelDataCore


class VideoDataCore:
    def __init__(self, response: dict):
        super(VideoDataCore, self).__init__(response)

        self.options = response["options"]
        self.mp4_videos = response["mp4_videos"]
        self.video_url = response["video_url"]
        self.channel = ChannelDataCore(response["channel"])

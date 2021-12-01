from .channels import ChannelDataCore
from .base import DataCore


class VideoDataCore(DataCore):
    def __init__(self, response: dict):
        super(VideoDataCore, self).__init__(response)

        self.options = response["options"]
        self.mp4_videos = response["mp4_videos"]
        self.video_url = response["video_url"]
        self.channel = ChannelDataCore(response["channel"])

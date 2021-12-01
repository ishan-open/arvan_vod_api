from .base import DataCore
from .channels import ChannelDataCore


class AudioDataCore(DataCore):
    def __init__(self, response: dict):
        super(AudioDataCore, self).__init__(response)

        self.mp4_audios = response['mp4_audios']
        self.audio_url = response['audio_url']
        self.channel = ChannelDataCore(response['channel'])

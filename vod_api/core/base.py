class MetaCore:
    def __init__(self, response: dict):
        self.response = response
        self.current_page = response['current_page']
        self.from_page = response['from']
        self.last_page = response['last_page']
        self.path = response['path']
        self.per_page = response['per_page']
        self.to = response['to']
        self.total = response['total']


class GeneralInfo:
    def __init__(self, response: dict):
        self.response = response
        if response:
            self.duration = response["duration"]
            self.format = response["format"]
            self.bit_rate = response["bit_rate"]
            self.size = response["size"]
        else:
            self.duration = None
            self.format = None
            self.bit_rate = None
            self.size = None


class VideoInfo:
    def __init__(self, response: dict):
        self.response = response
        if response:
            self.codec = response["codec"]
            self.width = response["width"]
            self.height = response["height"]
            self.frame_rate = response["frame_rate"]
            self.bit_rate = response["bit_rate"]
        else:
            self.codec = None
            self.width = None
            self.height = None
            self.frame_rate = None
            self.bit_rate = None


class AudioInfo:
    def __init__(self, response: dict):
        self.response = response
        if response:
            self.codec = response["codec"]
            self.sample_rate = response["sample_rate"]
            self.bit_rate = response["bit_rate"]
            self.channel_layout = response["channel_layout"]
        else:
            self.codec = None
            self.sample_rate = None
            self.bit_rate = None
            self.channel_layout = None


class FileInfo:
    def __init__(self, response: dict):
        self.response = response
        self.general = GeneralInfo(response.get("general"))
        self.audio = AudioInfo(response.get("audio"))
        self.video = VideoInfo(response.get("video"))


class DataCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response['id']
        self.title = response['title']
        self.description = response['description']
        self.file_info = FileInfo(response['file_info'])
        self.thumbnail_time = response['thumbnail_time']
        self.status = response['status']
        self.job_status_url = response['job_status_url']
        self.available = response['available']
        self.convert_mode = response['convert_mode']
        self.convert_info = response['convert_info']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.completed_at = response['completed_at']
        self.parallel_convert = response['parallel_convert']
        self.directory_size = response['directory_size']
        self.config_url = response['config_url']
        self.hls_playlist = response['hls_playlist']
        self.dash_playlist = response['dash_playlist']
        self.thumbnail_url = response['thumbnail_url']
        self.tooltip_url = response['tooltip_url']
        self.player_url = response['player_url']

class ProfileDataCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response['id']
        self.title = response['title']
        self.description = response['description']
        self.convert_mode = response['convert_mode']
        self.convert_info = response['convert_info']
        self.thumbnail_time = response['thumbnail_time']
        self.watermark = response['watermark']
        self.watermark_area = response['watermark_area']
        self.options = response['options']

class Base:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.auth = {"Authorization": api_key}
        self.base_url = "https://napi.arvancloud.com/vod/2.0"

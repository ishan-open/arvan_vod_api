class WatermarkDataCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response['id']
        self.title = response['title']
        self.description = response['description']
        self.url = response['url']
        self.available = response['available']

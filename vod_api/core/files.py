class FileCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response.get('id')
        self.url = response.get('url')
        self.filename = response.get('filename')

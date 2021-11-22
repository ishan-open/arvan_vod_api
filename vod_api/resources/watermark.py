from .base import Base


class Watermark(Base):
    def __init__(self, api_key: str):
        super(Watermark, self).__init__(api_key)

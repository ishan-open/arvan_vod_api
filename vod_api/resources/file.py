from .base import Base


class File(Base):
    def __init__(self, api_key: str):
        super(File, self).__init__(api_key)

from .base import Base


class Domain(Base):
    def __init__(self, api_key: str):
        super(Domain, self).__init__(api_key)

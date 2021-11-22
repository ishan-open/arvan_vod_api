from .base import Base


class GeneralReport(Base):
    def __init__(self, api_key: str):
        super(GeneralReport, self).__init__(api_key)

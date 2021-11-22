class Error(Exception):
    pass


class InvalidKeyError(Error):
    def __str__(self) -> str:
        return f"InvalidKeyError, ApiKey is Invalid or Expired!"
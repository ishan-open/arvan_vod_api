class Error(Exception):
    pass


class InvalidKeyError(Error):
    def __str__(self) -> str:
        return "InvalidKeyError, ApiKey is Invalid or Expired!"


class ArvanInternalError(Error):
    def __str__(self) -> str:
        return "ArvanInternalError, There is a problem in ArvanCloudApi, " \
                "or parameters have been defined incorrectly!"

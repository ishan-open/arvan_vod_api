class Error(Exception):
    pass


class InvalidKeyError(Error):
    def __str__(self) -> str:
        return "InvalidKeyError, ApiKey is Invalid or Expired!"


class ArvanInternalError(Error):
    def __str__(self) -> str:
        return "ArvanInternalError, There is a problem in ArvanCloudApi, " \
                "or parameters have been defined incorrectly!"


class InvalidParameterError(Error):
    def __init__(self, errors: dict):
        self.message = ""
        for key, value in errors.items():
            self.message += f"{key}: {''.join([i for i in value])} \n"

    def __str__(self) -> str:
        return self.message


class NotFoundError(Error):
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message


class InvalidOffsetError:
    def __str__(self) -> str:
        return "Invalid offset or offset is bigger than file size"

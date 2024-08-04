class ServiceException(Exception):

    def __init__(self, msg:str, http_erro_code) -> None:
        self.msg = msg
        self.http_erro_code = http_erro_code
        super().__init__(self.msg)
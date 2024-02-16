class Uri:
    def __init__(self, host: str, port) -> None:
        self.host = host
        self.port = port

    @property
    def http(self):
        return f'http://{self.host}:{self.port}'
    
    @property
    def ws(self):
        return f'ws://{self.host}:{self.port}'
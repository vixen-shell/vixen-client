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

class FrameCounter:
    def __init__(self) -> None: self.count: int = 0
    def increment(self): self.count += 1
    def decrement(self): self.count -= 1

    @property
    def value(self): return self.count

frameCounter = FrameCounter()
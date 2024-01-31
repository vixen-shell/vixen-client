class FramesCounter:
    def __init__(self) -> None: self.count: int = 0
    def increment(self): self.count += 1
    def decrement(self): self.count -= 1

    @property
    def value(self): return self.count

frameCounter = FramesCounter()
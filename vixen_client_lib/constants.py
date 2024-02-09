from .globals import Uri

API_URI = Uri('localhost', 6481)

def FRONT_URI(dev: bool):
    DIST_URI = Uri('localhost', 6492)
    DEV_URI = Uri('localhost', 5173)
    return DEV_URI if dev else DIST_URI
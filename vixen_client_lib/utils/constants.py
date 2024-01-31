FRONT_URL = {
    'release': 'http://localhost:6492',
    'dev': 'http://localhost:5173'
}

def mode(dev: bool):
    return 'dev' if dev else 'release'
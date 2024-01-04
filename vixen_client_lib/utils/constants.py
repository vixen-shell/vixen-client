FRONT_URL = {
    'release': 'http://localhost:8999',
    'dev': 'http://localhost:5173'
}

def mode(dev: bool):
    return 'dev' if dev else 'release'
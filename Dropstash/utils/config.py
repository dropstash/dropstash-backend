
def get_secret_key():
    # very raw dummy version
    key = ''
    with open('config/keys.cfg', 'r') as f:
        key = f.read()
    return key

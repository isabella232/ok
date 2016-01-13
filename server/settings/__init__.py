import os

try:
    import secret_keys as keys
except ImportError:
    keys = None

class Config:
    SECRET_KEY = 'samplekey'
    GOOGLE = {
        'consumer_key': os.getenv('GOOGLE_ID', 'fake'),
        'secret': os.getenv('GOOGLE_SECRET', 'fake')
    }

class LocalConfig(Config):
    DEBUG = True
    SECRET_KEY = 'Testing*ok*server*'
    RESTFUL_JSON = {'indent': 4}
    TESTING_LOGIN = True

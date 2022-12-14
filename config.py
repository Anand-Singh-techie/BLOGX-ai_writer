##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

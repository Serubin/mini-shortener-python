
class BaseConfig():
    DEBUG = False
    TESTING = False
    HASH_SIZE = 5

class DebugConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class TestingConfig(DebugConfig):
    DEBUG = False
    HASH_SIZE = 5 # Ensue this is 5


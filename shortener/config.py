
class BaseConfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    HASH_SIZE = 5

class DebugConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class TestConfig(DebugConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    HASH_SIZE = 5 # Ensue this is 5


import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    JSON_SORT_KEYS = False

class DevConfig(Config):
    DEBUG = True

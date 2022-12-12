import os

BASE_DIR = os.path.dirname(os.path.abspath('__name__'))
SECRET_KEY_OS = os.urandom(32)


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY_OS
    SECURITY_PASSWORD_SALT = 'dsffweewfweew'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'


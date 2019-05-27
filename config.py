import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/static/image'
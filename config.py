import os

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collins:qwertyui@localhost/pitchhs'
    UPLOADED_PHOTOS_DEST = 'app/static/photo'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'Done in 60 seconds'
    SENDER_EMAIL = 'kiprutohcollo@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://collins:qwertyui@localhost/pitchhs'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://collins:qwertyui@localhost/pitchhs'
config_options = {
    'development': DevConfig,
    'production': prodConfig,
    'test':TestConfig
}

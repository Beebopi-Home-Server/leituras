import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'tunelsecreto'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST_ADDR = '127.0.0.1'
    PORT = 5000

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'development-data.sqlite')


class ProductionConfig(Config):
    DATABASE_DIR = '/app/dados'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_DIR}/data.sqlite'
    HOST_ADDR = '0.0.0.0'



config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }

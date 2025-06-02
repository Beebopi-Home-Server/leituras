import threading
from flask import Flask
from flask_bootstrap import Bootstrap5
# from setuptools_scm import get_version
from config import config
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from os import mkdir

# __version__ = get_version()
__version__ = '0.1'

db = SQLAlchemy()

# Define os modelos do DB
from . import models

def create_app(config_name='default'):
    app = Flask(__name__)

    # Variáveis de configuração
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Inicia as extensões
    Bootstrap5(app)
    db.init_app(app)
    
    # Rotas Views
    from .routes_views import views_blueprint
    app.register_blueprint(views_blueprint)

    # Torna __version__ acessível para os templates
    @app.context_processor
    def inject_version():
        return { 'version': __version__ }

    # Cria o banco de dados
    database_dir = app.config.get('DATABASE_DIR')
    if database_dir and not Path(database_dir).exists():
        mkdir(app.config['DATABASE_DIR'])

    with app.app_context():
        db.create_all()


    # Cria a thread de escuta do mqtt
    print('Criando a thread de escutda MQTT')
    from .mqtt_listener import main
    threading.Thread(target=main, args=(app,), daemon=True).start()

    return app


# https://github.com/Workable/flask-log-request-id

import os, yaml
from logging.config import dictConfig
from flask_log_request_id import RequestID, RequestIDLogFilter
from dotenv import load_dotenv

class BaseConfig(object):
    load_dotenv(dotenv_path=f'.env')
    ENV = os.getenv('FLASK_ENV')

class DevelopmentConfig(BaseConfig):
    from config.development.orator import DATABASES  as orator_databases
    DEBUG = True
    TESTING = True
    # ORATOR_DATABASES = orator_databases

config = {
    "development": "app.config.DevelopmentConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name]) # object-based default configuration
    configure_logger(app)

def configure_logger(app):
    dictConfig(yaml.full_load(open(f'config/{os.getenv("FLASK_ENV")}/logging.conf')))
    RequestID(app)
    app.logger.addFilter(RequestIDLogFilter())

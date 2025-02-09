import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

from masoniteorm.connections import ConnectionResolver

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DATABASES = {
    'default': 'caas',
    'caas': {
        'driver': 'mysql',
        'host': os.getenv('CAAS_DB_HOST'),
        'database': os.getenv('CAAS_DB_NAME'),
        'user': os.getenv('CAAS_DB_USER'),
        'password': os.getenv('CAAS_DB_PASSWORD'),
        'prefix': ''
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)

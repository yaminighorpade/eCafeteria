import datetime
import os

# Service configuration
SERVICE_NAME = 'registration_api'
SERVICE_VERSION = '0.0.1'
SERVICE_DEPLOYMENT_TIMESTAMP = datetime.datetime.now()
ENVIRONMENT = 'local'

# API configuration
API_PREFIX = '/registration'

# Swagger Root Folder
SWAGGER_UI_URL = f'{API_PREFIX}/docs/swagger'
REDOC_URL = f'{API_PREFIX}/docs/redoc'

# local uvicorn configuration
HOST = '127.0.0.1'
PORT = 8080
DEBUG = 'true'

# PostGreSQL Connection Details
DB_HOST = '127.0.0.1'
DB_PORT = 5432
DATABASE = 'postgres'
DB_USER = 'postgres'
DB_PWD = ''


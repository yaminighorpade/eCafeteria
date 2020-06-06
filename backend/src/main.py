import logging
import uvicorn
from fastapi import FastAPI

from src.config import config
from src.services import services

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f'Starting up {config.SERVICE_NAME} v{config.SERVICE_VERSION} on stage {config.ENVIRONMENT}')

app = FastAPI(title="Registration",
              description="API to register employee/vendors",
              version=config.SERVICE_VERSION,
              docs_url=config.SWAGGER_UI_URL,
              redoc_url=config.REDOC_URL,
              openapi_url=f"{config.SWAGGER_UI_URL}/openapi.json",
              )

# integrate the endpoints and services
services.define_services(app)

if __name__ == '__main__':
    if config.ENVIRONMENT == 'local':
        uvicorn.run(app, host=config.HOST, port=config.PORT, debug=config.DEBUG)
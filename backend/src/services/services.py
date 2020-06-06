import logging

from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from src.config import config
from src.model.system_info import SystemInfo
from src.model.request_model import EmployeeRegisterRequest,VendorRegisterRequest
import time
from src.model.postgres_model import DbConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ADMIN_SERVICES = 'Administration'
GET_SERVICES = 'StatusCheck'
current_time = time.time()


def define_services(app):
    define_master_services(app)
    __define_admin_endpoints(app)


def __define_admin_endpoints(app):
    @app.get("/.well-known/info", response_model=SystemInfo, name='System Info', tags=[API_ADMIN_SERVICES])
    def get_system_info():
        logger.info('Getting information about the deployed service')

        info = {
            'name': config.SERVICE_NAME,
            'version': config.SERVICE_VERSION,
            'deployed': config.SERVICE_DEPLOYMENT_TIMESTAMP
        }

        return info

    @app.get("/.well-known/live", tags=[API_ADMIN_SERVICES])
    def liveness_check():
        logger.debug('Liveness check')

        return 'OK'

    @app.get("/.well-known/ready", tags=[API_ADMIN_SERVICES])
    def readiness_check():
        logger.debug('Readiness check')

        return 'OK'

    return


def define_master_services(app):
    @app.post(config.API_PREFIX + "/employee",
          name='Register an Employee',
          description='Register Employee to e-cafeteria application'
          )
    def register_employee(request:EmployeeRegisterRequest):
        query = f"INSERT INTO employee(employee_id,employee_name, employee_base_location, employee_current_location,created_on) VALUES (" \
            f"{request.employee_id},'{request.employee_name}','{request.employee_base_location}','{request.employee_current_location}'," \
            f" CURRENT_TIMESTAMP )"
        db_object = DbConnection()
        db_object.apply_data(query)
        response = \
            {
                u"status":"Success",
            }
        return JSONResponse(response)

    @app.post(config.API_PREFIX + "/vendor",
          name='Register a Vendor',
          description='Register Vendor to e-cafeteria application'
          )
    def register_employee(request:VendorRegisterRequest):
        query = f"INSERT INTO vendor(vendor_name,vendor_location, cafeteria_location,created_on) VALUES (" \
            f"'{request.vendor_name}','{request.vendor_location}','{request.cafeteria_location}', CURRENT_TIMESTAMP)"
        db_object = DbConnection()
        db_object.apply_data(query)
        response = \
            {
                u"status":"Success",
            }
        return JSONResponse(response)

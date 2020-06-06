from pydantic import BaseModel


class EmployeeRegisterRequest(BaseModel):
    employee_id: int
    employee_name: str
    employee_base_location: str
    employee_current_location: str


class VendorRegisterRequest(BaseModel):
    vendor_name: str
    vendor_location: str
    cafeteria_location: str

class EmployeeDeRegisterRequest(BaseModel):
    employee_id: str


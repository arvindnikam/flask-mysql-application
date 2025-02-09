from app.models import Employee
from app.exceptions import InvalidDataError

def call(employee_id):
    if not (employee := Employee.find(employee_id)):
        raise InvalidDataError('Invalid employee id')

    return employee.serialize()

from app.models import Employee
from app.exceptions import InvalidDataError

def call(employee_id, request):
    if not (employee := Employee.find(employee_id)):
        raise InvalidDataError('Invalid employee id')

    employee.update(request)

    return employee.serialize()

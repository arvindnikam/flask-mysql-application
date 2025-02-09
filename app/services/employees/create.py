from app.models import Employee

def call(request):
    employee = Employee.create(request)
    return employee.serialize()

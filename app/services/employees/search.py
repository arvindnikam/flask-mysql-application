from app.models import Employee
from app.lib.helpers.search_helper import parse_conditions

def call(conditions, offset=None, limit=None, sort_column=None, sort_order=None):
    search_conditions = parse_conditions(conditions)
    employees = Employee.where(conditions).offset(offset).limit(limit).order_by(sort_column, sort_order).get()
    total = Employee.where(conditions).count()

    return {
        "employees": employees.serialize(),
        "offset": offset,
        "limit": limit,
        "sort_column": sort_column,
        "sort_order": sort_order,
        "count": employees.count(),
        "total": total
    }

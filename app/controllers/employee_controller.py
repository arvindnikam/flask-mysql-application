from flask import request
from app.lib.helpers.response_helper import generate_response

def before_request():
    pass

def create():
    from app.services.employees import create as create_service

    request_json = request.json.get('employee', {})
    response_data = create_service.call(request_json)
    generate_response(success=True, response_data={'status': 'success', 'message': "employee created successfully", "data": response_data})

def show(employee_id):
    from app.services.employees import show as show_service

    response_data = show_service.call(employee_id)
    generate_response(success=True, response_data={'status': 'success', 'message': "employee fetched successfully", "data": response_data})

def update(employee_id):
    from app.services.employees import update as update_service

    request_json = request.json.get('employee', {})
    response_data = update_service.call(employee_id, request_json)
    generate_response(success=True, response_data={'status': 'success', 'message': "employee updated successfully", "data": response_data})

def search():
    from app.services.employees import search as search_service
    from app.lib.helpers.search_helper import get_search_options

    request_json = request.json
    conditions = request_json.get('conditions', {})
    search_options = get_search_options(request_json)

    response_data = search_service.call(conditions, **search_options)
    generate_response(success=True, response_data={'status': 'success', 'message': "employees found", "data": response_data})

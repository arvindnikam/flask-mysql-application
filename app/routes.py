from flask import Blueprint

## Base
from app.controllers import base_controller
base_blueprint = Blueprint('base_blueprint', __name__)
base_blueprint.route('/', methods=['GET'])(base_controller.index)
# ------------------------------------------------------------------------------------------------------------------------------------ #

## Employee
from app.controllers import employee_controller
employee_blueprint = Blueprint('employee_blueprint', __name__)
employee_blueprint.before_request(employee_controller.before_request)
employee_blueprint.route('/create', methods=['POST'])(employee_controller.create)
employee_blueprint.route('/<int:employee_id>', methods=['GET'])(employee_controller.show)
employee_blueprint.route('/<int:employee_id>/update', methods=['PUT', 'PATCH'])(employee_controller.update)
employee_blueprint.route('/search', methods=['POST'])(employee_controller.search)
# ------------------------------------------------------------------------------------------------------------------------------------ #

def initialize_routes(app):
    @app.before_request
    def before_request(): base_controller.before_request()
    @app.after_request
    def after_request(response): return base_controller.after_request(response)

    app.register_blueprint(base_blueprint)
    app.register_blueprint(employee_blueprint, url_prefix='/api/v1/employees')

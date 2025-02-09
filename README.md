# Flask Employee API

## Overview

This is a Flask-based REST API that manages employee records using Masonite ORM with a MySQL database. The application provides various endpoints for creating, retrieving, updating, and searching for employees.

## Features

- Uses Masonite ORM for database interactions.
- Stores employee data in a MySQL database.
- Provides CRUD operations for employee records.
- Uses Flask Blueprints for modular architecture.
- Implements middleware for pre- and post-request processing.

## Installation

### Prerequisites

- Python 3.7+
- Flask
- Masonite ORM (https://orm.masoniteproject.com/)
- MySQL Server

### Setup

1. Clone the repository:
   ```sh
   git clone git@github.com:arvindnikam/flask-base-application.git
   cd flask-base-application
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure MySQL database:
   - Update `.env` with your MySQL credentials:
   - Run migrations:
     ```sh
     masonite-orm migrate
     ```
5. Run the application:
   ```sh
   flask run
   ```

## API Endpoints

### Base Endpoint

| Method | Route | Description          |
| ------ | ----- | -------------------- |
| GET    | `/`   | Returns health check |

### Employee Endpoints

| Method    | Route                               | Description                   |
| --------- | ----------------------------------- | ----------------------------- |
| POST      | `/api/v1/employees/create`          | Creates a new employee record |
| GET       | `/api/v1/employees/<int:id>`        | Retrieves an employee by ID   |
| PUT/PATCH | `/api/v1/employees/<int:id>/update` | Updates an employee record    |
| POST      | `/api/v1/employees/search`          | Searches for employees        |

## Middleware

- `before_request`: Executed before every request to handle pre-processing.
- `after_request`: Executed after every request for post-processing.

## Project Structure

```
flask-base-application
|-- app/
|   |-- controllers/
|   |   |-- base_controller.py
|   |   |-- employee_controller.py
|   |-- db/
|   |   |-- __init__.py
|   |-- exceptions/
|   |   |-- __init__.py
|   |-- lib/
|   |   |-- helpers/
|   |       |-- response_helper.py
|   |-- models/
|   |   |-- employee.py
|   |-- services/
|   |   |-- employees/
|   |       |-- create.py
|   |       |-- search.py
|   |       |-- show.py
|   |       |-- update.py
|   |-- __init__.py
|   |-- config.py
|   |-- routes.py
|-- config/
|   |-- development/
|   |   |-- logging.cong
|-- log/
|-- .env
|-- requirements.txt
|-- wsgi.py
```

## License

This project is licensed under the MIT License.


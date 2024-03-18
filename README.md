# Corporate Asset Tracking System

## Project Overview:
The Corporate Asset Tracking System is a Django application designed to track corporate assets such as phones, tablets, and laptops assigned to employees. It provides a user-friendly interface for managing companies, employees, and devices, along with a powerful API for seamless integration with other systems.

## Features:
- CRUD operations for managing companies, employees, and devices.
- API endpoints for programmatic access to data.
- Automatic generation of API documentation using Django Rest Swagger.
- Comprehensive unit tests to ensure code reliability and functionality.
- Well-commented codebase for easy maintenance and understanding.

## Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/lsshormi/Corporate_CURD_Project.git

2. Navigate to the project directory:
   - cd corporate-asset-tracking

3. Create and activate a virtual environment (optional):
   - python -m venv venv
   - source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install dependencies:
   - pip install -r requirements.txt

5. Apply migrations:
   - python manage.py migrate

## Usage:
1. Start the Django development server:
   - python manage.py runserver

2. Access the web interface:
   - Open a web browser and navigate to 'http://localhost:8000/'.

3. Access the API endpoints:
   - Companies: 'http://localhost:8000/companies/'
   - Employees: 'http://localhost:8000/employees/'
   - Devices: 'http://localhost:8000/devices/'

Use the web interface or API endpoints to perform CRUD operations on companies, employees, and devices.

4. Access API documentation:
   - Visit 'http://localhost:8000/swagger/' to view auto-generated API documentation using Django Rest Swagger.

## Unit Tests:
The project includes comprehensive unit tests covering models, views, and APIs. To run the tests, execute the following command:
   - python manage.py test

## Contributing:
Contributions to the Corporate Asset Tracking System are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve the project.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




# Foxiomreport

Foxiomreport is a Flask-based web application designed to generate sales reports from a SQL Server database. The application exposes the results through a RESTful API. This project follows a structured layout and includes unit tests to verify the functionality of both the report generation and the database connection.


## Installation

```bash
git clone https://github.com/your-username/foximreport.git
cd foximreport
poetry shell
poetry install
```

## Usage 

1. Set up the required environment variables by creating a .env file in the project root with the following content:
  
DATABASE_DRIVER=<your_database_driver>
DATABASE_SERVER=<your_database_server>
DATABASE_NAME=<your_database_name>
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_INSTANCE=<your_database_instance>

2. Run the Flask application:
```bash
python app.py
```

3. Access the API endpoint at http://127.0.0.1:5000/sales/reports to retrieve the sales report in CSV format.

Generate a report:

GET /sales/reports

    Returns CSV data containing:

    Group1
    Category
    Customer
    GSTIN
    Address
    Product
    Grand Total

## Project Structure
- app.py: Flask application responsible for exposing the API endpoint.
- api/db.py: Database-related functions for generating sales reports.
- tests/: Directory containing unit tests for the application.
- pyproject.toml: Poetry configuration file specifying project dependencies.

## Database Connection
The api/db.py module contains the get_db_connection function, which establishes a connection to the SQL Server database using the specified environment variables.

## API Endpoint
The /sales/reports endpoint in app.py uses the generate_report function from api/db.py to fetch sales data from the database and returns the report in CSV format through the API.

## Testing
The tests/ directory includes unit tests for the application. Run the tests using the following command:
```bash
python run pytest
```

### Dependencies

- Python 3.10
- Flask 2.2.2
- pyodbc 4.0.35
- environs
- pytest 7.2.0
Add more dependencies use 
```bash
poetry add package_name
```

## Start the API server

```bash
python app.py
```

The API will run on port 5000 by default.

## License
This project uses the MIT License.

## Contact
Author - AkhilKrishnan - akhilkrishnan295@gmail.com

Let me know if you have any other questions!
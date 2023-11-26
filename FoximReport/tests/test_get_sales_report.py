import pytest
import requests
from foximreport.app import app

# Fixture to create a test client for the Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test function to check if the /get_report endpoint returns a valid CSV response
def test_get_report(client):
    # Make a GET request to the /get_report endpoint
    response = client.get('/get_report')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response content type is CSV
    assert response.headers['Content-Type'] == 'text/csv'

    # Check if the response has the correct CSV headers
    expected_headers = [
        "Group1", "CATEGORY", "CUSTOMER", "GSTN", "ADDRESS", "PRODUCT", "GRAND TOTAL (SUM)"
    ]
    assert response.data.decode().splitlines()[0].split(',') == expected_headers




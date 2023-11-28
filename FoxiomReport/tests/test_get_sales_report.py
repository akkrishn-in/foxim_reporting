import json

import pytest
from foxiomreport.app import app
from foxiomreport.api.db import get_db_connection


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_report(client):
    response = client.get("/sales/reports")

    assert response.status_code == 200

    data = json.loads(response.data)
    assert "report" in data
    report = data["report"]

    # Check report is a valid CSV
    lines = report.split("\n")
    assert lines[0].split(",") == [
        "Group1",
        "CATEGORY",
        "CUSTOMER",
        "GSTN",
        "ADDRESS",
        "PRODUCT",
        "GRAND TOTAL (SUM)",
    ]


def test_db_connection():
    # Check connection
    conn = get_db_connection()
    assert conn is not None

    # Run a test query
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1

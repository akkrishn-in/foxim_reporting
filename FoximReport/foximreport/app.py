from api.db import generate_report
from io import StringIO
import csv
from flask import Flask, Response

app = Flask(__name__)


# Endpoint to get the report
@app.route("/get_report", methods=["GET"])
def get_report():
    csv_data = generate_report()

    csv_output = StringIO()
    csv_writer = csv.writer(csv_output)

    csv_writer.writerow(
        [
            "Group1",
            "CATEGORY",
            "CUSTOMER",
            "GSTN",
            "ADDRESS",
            "PRODUCT",
            "GRAND TOTAL (SUM)",
        ]
    )

    for row in csv_data:
        csv_writer.writerow(row)

    csv_output.seek(0)

    return Response(
        csv_output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=report.csv"},
    )

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
import csv
from io import StringIO
from api.db import generate_report


app = Flask(__name__)


@app.route("/sales/reports", methods=["GET"])
def get_report():
    data = generate_report()

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

    for row in data:
        csv_writer.writerow(row)

    output = csv_output.getvalue()

    return jsonify({"report": output})


if __name__ == "__main__":
    app.run()

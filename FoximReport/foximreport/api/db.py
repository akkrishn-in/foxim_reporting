import pyodbc
from environs import Env


# Get environment variables
env = Env()
env.read_env()


# Function to create a database connection
def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={env('DATABASE_DRIVER')};"
        f"SERVER={env('DATABASE_SERVER')};"
        f"DATABASE={env('DATABASE_NAME')};"
        f"UID={env('DATABASE_USER')};"
        f"PWD={env('DATABASE_PASSWORD')};"
        f"INSTANCE={env('DATABASE_INSTANCE')};"
    )
    conn.autocommit = True
    return conn


def generate_report():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """ SELECT 
    PG.product_group_Id AS Group1,
    PC.product_category_id AS CATEGORY,
    SM.customer_name AS CUSTOMER,
    SM.gst_no AS GSTIN,
    SM.customer_address AS "ADDRESS",
    PM.product_name AS PRODUCT,
    CAST(SUM(SM.grand_total) AS INT) AS "GRAND TOTAL(SUM)"
    FROM tblSalesMaster AS SM
    INNER JOIN tblSalesDetails AS SD
    ON SD.entry_id_code = SM.entry_no
    INNER JOIN tblProductMaster AS PM
    ON PM.product_Id = SD.item_id
    INNER JOIN tblProductGroup AS PG
    ON PG.product_group_Id = PM.product_group_id
    INNER JOIN tblProductAttribute AS PA
    ON PA.product_Id = PM.product_Id
    INNER JOIN tblProductCategory AS PC
    ON PC.product_category_id = PA.pro_category_id
    INNER JOIN tblLedgerNames AS LN
    ON LN.ledger_id = SM.account_id
    GROUP BY
        PG.product_group_Id, PC.product_category_id, SM.customer_name, SM.gst_no,
        SM.customer_address, PM.product_name
    ORDER BY
        PG.product_group_Id, PC.product_category_id, SM.customer_name, SM.gst_no,
                SM.customer_address, PM.product_name
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    return rows

import pyodbc


def db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LAPTOP-3RKKTDMH;"
        "DATABASE={test};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conn
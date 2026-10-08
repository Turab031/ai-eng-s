import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RailwayDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

print("Connected successfully!")

conn.close()
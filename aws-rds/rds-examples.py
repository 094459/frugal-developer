import pymysql
import boto3
import json

# RDS connection details (hardcoded, which is bad for security too!)
db_host = "your-db-instance.rds.amazonaws.com"
db_user = "admin"
db_password = "yourpassword"
db_name = "yourdatabase"

def lambda_handler(event, context):
    # Inefficient: Creating a new database connection on every Lambda execution
    conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = conn.cursor()

    # Inefficient: Running a simple query but opening/closing a connection each time
    cursor.execute("SELECT * FROM users WHERE username = %s", ("john_doe",))
    result = cursor.fetchall()

    conn.close()  # Closing connection after every invocation (bad for performance)

    return {"statusCode": 200, "body": json.dumps(result)}

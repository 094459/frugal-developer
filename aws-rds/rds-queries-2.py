import pymysql

# RDS Connection
conn = pymysql.connect(
    host="your-db-instance.rds.amazonaws.com",
    user="your_user",
    password="your_password",
    database="your_database"
)

def fetch_all_data():
    """Fetching all data multiple times instead of caching"""
    with conn.cursor() as cursor:
        for _ in range(1000):  # Repeating the same query 1000 times
            cursor.execute("SELECT * FROM large_table;")  # Fetching entire table every time
            results = cursor.fetchall()
            print(f"Fetched {len(results)} rows")  # Pointless repeated prints

# Run query
fetch_all_data()

import pymysql
import time

# RDS Connection
conn = pymysql.connect(
    host="your-db-instance.rds.amazonaws.com",
    user="your_user",
    password="your_password",
    database="your_database"
)

def get_top_products():
    """Inefficient: Fetching from RDS every time, even if data rarely changes"""
    with conn.cursor() as cursor:
        cursor.execute("SELECT product_id, name FROM products ORDER BY sales DESC LIMIT 10;")
        result = cursor.fetchall()
    return result

start_time = time.time()
print(get_top_products())  # Fetch from RDS (Slow, Expensive)
print("Time taken:", time.time() - start_time)

import pymysql

# RDS Connection
conn = pymysql.connect(
    host="your-db-instance.rds.amazonaws.com",
    user="your_user",
    password="your_password",
    database="your_database"
)

def fetch_users_one_by_one():
    """Fetching one row at a time instead of batching"""
    with conn.cursor() as cursor:
        cursor.execute("SELECT user_id FROM users;")  # Fetch user IDs first
        user_ids = cursor.fetchall()

        for user_id in user_ids:
            cursor.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))  # One query per user
            user_data = cursor.fetchone()
            print(user_data)

# Run function
fetch_users_one_by_one()

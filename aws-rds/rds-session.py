import pymysql

def store_user_session(user_id, session_data):
    """Inefficient: Storing every user session in RDS"""
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO sessions (user_id, session_data) VALUES (%s, %s) ON DUPLICATE KEY UPDATE session_data = %s",
            (user_id, session_data, session_data)
        )
        conn.commit()

store_user_session(123, "user_logged_in")

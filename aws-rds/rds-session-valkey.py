import pymysql
import valkey

# Initialize Valkey client
cache = valkey.StrictValkey(host="your-valkey-endpoint", port=6379, db=0)

def store_user_session_cached(user_id, session_data):
    """Optimized: Store user session in Valkey instead of RDS"""
    cache_key = f"session:{user_id}"
    cache.setex(cache_key, 3600, session_data)  # Store for 1 hour

store_user_session_cached(123, "user_logged_in")

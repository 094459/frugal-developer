import pymysql
import valkey  # Using Valkey instead of Redis
import json

# Initialize Valkey client
cache = valkey.StrictValkey(host="your-valkey-endpoint", port=6379, db=0)

# RDS Connection
conn = pymysql.connect(
    host="your-db-instance.rds.amazonaws.com",
    user="your_user",
    password="your_password",
    database="your_database"
)

def get_top_products_cached():
    """Optimized: Fetch from Valkey cache if available, else fetch from RDS and cache result"""
    cache_key = "top_products"
    
    cached_data = cache.get(cache_key)
    if cached_data:
        return json.loads(cached_data)  # Return cached data if available

    # Fetch from RDS (only if not cached)
    with conn.cursor() as cursor:
        cursor.execute("SELECT product_id, name FROM products ORDER BY sales DESC LIMIT 10;")
        result = cursor.fetchall()
    
    # Store result in Valkey with 10-minute expiration
    cache.setex(cache_key, 600, json.dumps(result))
    
    return result

print(get_top_products_cached())  # Fast, Cached Query

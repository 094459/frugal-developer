Why This is Expensive:

❌ New database connection on every execution → Adds latency and increases RDS cost due to excessive connections.
❌ Increased AWS Lambda cold starts → Each invocation has to reconnect to RDS, increasing execution time.
❌ No connection pooling → Inefficient use of database connections.

✅ Optimized Approach:

Use Amazon RDS Proxy to reuse connections efficiently.
Use persistent connections with connection pooling libraries like SQLAlchemy or aiomysql.

**Optimisation**

Many applications open and close database connections frequently, increasing RDS costs due to:

High connection overhead
Long query execution times
Increased CPU usage on RDS

Use connection pooling to reuse database connections instead of creating a new one for every query.

```
import psycopg2
from psycopg2 import pool

# Using a connection pool instead of opening/closing connections for every query
db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,  # Maximum number of reusable connections
    user="your_user",
    password="your_password",
    host="your-db-instance.rds.amazonaws.com",
    database="your_database"
)

def query_db():
    conn = db_pool.getconn()  # Get a connection from the pool
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE active = true;")
            results = cursor.fetchall()
            return results
    finally:
        db_pool.putconn(conn)  # Release the connection back to the pool

# Run query
print(query_db())

# Close the pool when done
db_pool.closeall()

```

Why This Optimizes RDS Costs

✅ Reduces connection overhead → Avoids frequent connection setups.
✅ Improves performance → Queries execute faster due to connection reuse.
✅ Lowers RDS CPU usage → Reduces unnecessary instance load.



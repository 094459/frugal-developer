> s3-api-example

💸 Why This is Expensive
❌ Every call incurs an API request (list_objects_v2).
❌ Repeatedly listing all objects is inefficient if objects are rarely deleted.
❌ Costs grow over time if called on a schedule (e.g., every hour).

> s3-api-fix-example

✅ Why This is Cost-Effective
✅ Reduces API calls by caching results.
✅ Uses S3 Inventory Reports (if implemented).
✅ Only refreshes when needed (e.g., once a day).
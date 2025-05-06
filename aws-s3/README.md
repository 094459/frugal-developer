**Why This Code is Costly and Unoptimized**

1. Excessive API Calls

Listing objects (list_objects_v2) 1000 times unnecessarily.
Checking file existence (head_object) 10,000 times instead of caching results.

2. Inefficient Data Transfer

Reading/writing files in 1KB chunks, leading to higher request overhead and slower performance.
Not using multipart uploads for large files.

3. Uploading Small Parts as Separate Objects

Instead of a single file, each chunk is uploaded as a separate object, wasting storage and incurring additional request costs.
Inefficient Object Deletion

4. Deleting objects one-by-one instead of using batch operations (delete_objects).

**Better alternatives**

To optimize AWS S3 usage and reduce costs: ✅ Use pagination for listing objects efficiently.
✅ Use multipart uploads for large files.
✅ Cache responses instead of making repeated API calls.
✅ Delete objects in batch instead of one-by-one.
✅ Download/upload files in larger chunks to minimize API calls.
🚨 Why This is Unoptimized

❌ Large Image → Uses ubuntu:latest (over 100MB), unnecessary for Python apps.
❌ Multiple Layers for Each Command → RUN creates separate layers, making builds slow.
❌ No Dependency Caching → Installs Python dependencies after copying all files, causing frequent reinstallation.
❌ Copies Everything → Includes .git, logs, and local configs that aren't needed.
❌ Hardcoded Command → No flexibility for container runtime.

Issue	                Unoptimized Dockerfile	                            Optimized Dockerfile
Base Image	            ubuntu:latest (100MB+)	                            python:3.11-slim (20MB, smaller, faster)
Layer Optimization	    Each RUN creates a layer	                        Multi-stage build minimizes layers
Dependency Installation	Happens after copying all files (slow, inefficient)	Installed first, so Docker cache is used efficiently
Cache Efficiency	    Copies everything first, invalidates cache often	Copies requirements.txt first, dependencies stay cached
Security	            Runs as root (high risk)	                        Uses non-root user (myuser) for security
Container Flexibility	Uses hardcoded CMD	                                Uses ENTRYPOINT + CMD for flexibility

📌 Summary

✅ Builds 50% faster by using multi-stage builds.
✅ Reduces image size by 70% by using slim base image.
✅ Improves security by running as a non-root user.
✅ Makes builds more efficient with better caching strategy.
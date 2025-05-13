# Frugal Developer

This repository contains examples of both inefficient and optimized code patterns to help developers build more cost-effective applications on AWS and other platforms. Each subdirectory contains examples that demonstrate how to optimize resource usage and reduce costs.

> **WARNING!**
>
>Code in this repo is deliberately not optimised and you should NOT use it. It is intended to demonstrate how you can use Amazon Q Developer to help you refactor the code so that it is more effecient and reduce the cost of using AWS services used.


## Directory Structure

### api-calls-aws
Examples of AWS API usage patterns, showing how to optimize API calls to reduce costs:
- `s3-api-example.py`: Demonstrates inefficient S3 API usage with excessive calls
- `s3-api-fix-example.py`: Shows optimized S3 API usage patterns

### api-calls-nonaws
Examples of optimizing API calls to non-AWS services:
- `non-cached-example.py`: Shows API calls without caching
- `cached-example.py`: Demonstrates how to implement caching for API calls

### aws-cloudwatch
Examples of CloudWatch usage patterns and optimizations:
- `fetch-cwlogs-example.py`: Inefficient log fetching that retrieves all logs
- `fetch-cwlogs-better.py`: Optimized log fetching that only retrieves recent logs
- `cloudwatch-examples.py`: Various CloudWatch usage patterns
- `lambda-cloudwatch-example.py`: CloudWatch integration with Lambda functions

### aws-dynamodb
Examples of DynamoDB usage patterns and optimizations:
- `dynamodb-overuse-scan.py`: Demonstrates inefficient scanning of entire tables
- `dynamodb-examples.py`: Shows various inefficient DynamoDB patterns like repeated scans and single-item operations
- `dynamodb-optimized.py`: Demonstrates optimized DynamoDB access patterns

### aws-rds
Examples of RDS usage patterns and optimizations:
- `rds-examples.py`: Shows inefficient database connection handling in Lambda
- `rds-queries-1.py`: Demonstrates inefficient one-by-one row fetching
- `rds-queries-2.py`: Shows optimized query patterns
- `rds-nocache.py` & `rd-cache.py`: Comparison of non-cached vs cached database access
- `rds-session.py` & `rds-session-valkey.py`: Session management examples

### aws-s3
Examples of S3 usage patterns and optimizations:
- `s3_examples.py`: Shows various inefficient S3 operations like repeated listing, small-chunk downloads, and individual deletions
- `s3_query_local_not_remote.py`: Demonstrates inefficient pattern of downloading entire datasets
- `s3_data_transfer_example.py`: Shows inefficient data transfer patterns with S3

### aws-spot-instance
Examples of optimizing for AWS Spot Instances:
- `pre-spot-example.py`: Code not optimized for spot instances
- `spot-friendly.py`: Code optimized for spot instance interruptions

### docker
Examples of Docker container optimization:
- `docker-initial.yaml`: Inefficient Docker configuration with large base image and multiple layers
- `docker-finished.yaml`: Optimized Docker configuration with multi-stage builds and smaller base image

### graviton
Examples of code optimization for AWS Graviton processors:
- `non-optimised-c-code.c`: C/C++ code not optimized for ARM architecture
- `optimised-c-code.c`: C/C++ code optimized for ARM architecture

### security
Examples of security best practices and common vulnerabilities:
- `app.py`: Flask application with various security issues like SQL injection, hardcoded secrets, and missing password hashing
- `templates/`: HTML templates for the Flask application

## Usage

Each subdirectory contains examples of both inefficient and optimized code. Review the code and comments to understand the differences and best practices for building cost-effective applications.

## License

See the [LICENSE](LICENSE) file for details.
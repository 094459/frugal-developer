# Insecure Messaging Application

This is a deliberately insecure Flask application created for educational purposes to demonstrate common security vulnerabilities.

## WARNING

**DO NOT USE THIS CODE IN PRODUCTION ENVIRONMENTS**

This application contains numerous security vulnerabilities that would put real users and systems at risk. It is intended solely for educational purposes to demonstrate what NOT to do when developing web applications.

## Security Vulnerabilities Demonstrated

1. **SQL Injection**: Using string formatting to build SQL queries instead of parameterized queries
2. **No Password Hashing**: Storing passwords in plaintext
3. **Hardcoded Secrets**: Secret key directly in the source code
4. **Cross-Site Scripting (XSS)**: Rendering unsanitized user input with the `safe` filter
5. **Insecure Deserialization**: Using Python's pickle module to deserialize user-provided data
6. **Missing Authentication**: No proper session management
7. **Missing Authorization**: Admin panel accessible to all logged-in users
8. **Debug Mode in Production**: Running with debug=True
9. **Binding to All Network Interfaces**: Using host='0.0.0.0'
10. **No Input Validation**: Accepting any input without validation
11. **No CSRF Protection**: No protection against Cross-Site Request Forgery

## Setup and Running

1. Install required packages:
   ```
   pip install flask
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access the application at http://localhost:5000

## Learning Resources

For information on how to properly secure web applications, please refer to:

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Flask Security Documentation](https://flask.palletsprojects.com/en/2.0.x/security/)
- [Web Application Security Best Practices](https://cheatsheetseries.owasp.org/)
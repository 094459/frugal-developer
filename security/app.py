from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
import pickle
import base64

app = Flask(__name__)
# BAD PRACTICE: Hardcoded secret key in source code
app.secret_key = "super_secret_key_123456"

# BAD PRACTICE: Database connection without proper error handling
def get_db():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn

# BAD PRACTICE: Not using parameterized queries
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        sender TEXT,
        recipient TEXT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # BAD PRACTICE: SQL Injection vulnerability
        conn = get_db()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid credentials'
    
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # BAD PRACTICE: No password hashing
        conn = get_db()
        cursor = conn.cursor()
        try:
            # BAD PRACTICE: SQL Injection vulnerability
            query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            cursor.execute(query)
            conn.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            error = 'Username already exists'
        finally:
            conn.close()
    
    return render_template('register.html', error=error)

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    recipient = request.form['recipient']
    message = request.form['message']
    sender = session['username']
    
    # BAD PRACTICE: No input validation
    conn = get_db()
    cursor = conn.cursor()
    # BAD PRACTICE: SQL Injection vulnerability
    query = f"INSERT INTO messages (sender, recipient, message) VALUES ('{sender}', '{recipient}', '{message}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    flash('Message sent!')
    return redirect(url_for('index'))

@app.route('/messages')
def messages():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    conn = get_db()
    cursor = conn.cursor()
    # BAD PRACTICE: SQL Injection vulnerability
    query = f"SELECT * FROM messages WHERE recipient = '{username}' ORDER BY timestamp DESC"
    cursor.execute(query)
    messages = cursor.fetchall()
    conn.close()
    
    return render_template('messages.html', messages=messages)

@app.route('/user_profile', methods=['GET', 'POST'])
def user_profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # BAD PRACTICE: Insecure deserialization
        user_data = request.form.get('user_data')
        if user_data:
            try:
                # BAD PRACTICE: Unsafe deserialization of user input
                user_obj = pickle.loads(base64.b64decode(user_data))
                return render_template('profile.html', user_data=user_obj)
            except:
                flash('Invalid user data')
    
    return render_template('profile.html')

@app.route('/admin')
def admin():
    # BAD PRACTICE: No proper authorization checks
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    # BAD PRACTICE: Debug mode enabled in production
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='templates')
app.secret_key = "your_secret_key"  # Required for flash messages

# Function to initialize the SQLite database
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        
        # Create tables for Donor and Organization signups if they don't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS Donor (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            contact TEXT NOT NULL,
                            user_type TEXT DEFAULT 'donor')''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Organization (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            unique_id TEXT NOT NULL,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            contact TEXT NOT NULL,
                            user_type TEXT DEFAULT 'org')''')

        conn.commit()

# Initialize database
init_db()

@app.route('/')
def landing_page():
    # Serve landing_page/index.html from the 'landing_page' folder
    return render_template('landing_page/index.html')

# Donor signup page
@app.route('/donor_signup_page')
def donor_signup_page():
    return render_template('Module_A/Donor_dashboard/signup.html')

# Organization signup page
@app.route('/organisation_signup_page')
def organisation_signup_page():
    return render_template('Module_C/organisation_login_signup/signup.html')

# Handle Donor signup form submission
@app.route('/donor_signup', methods=['POST'])
def donor_signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    contact = request.form['contact']

    # Check if email already exists in Donor table
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Donor WHERE email = ?", (email,))
        existing_donor = cursor.fetchone()
        
        if existing_donor:
            flash("Email already exists! Please use a different email.", "error")
            return redirect(url_for('donor_signup_page'))
        
        # Insert new donor data into Donor table
        cursor.execute("INSERT INTO Donor (name, email, password, contact) VALUES (?, ?, ?, ?)", 
                       (name, email, password, contact))
        conn.commit()
    
    flash("Donor signed up successfully!")
    return redirect(url_for('landing_page'))

# Handle Organization signup form submission
@app.route('/organisation_signup', methods=['POST'])
def organisation_signup():
    unique_id = request.form['uniqueId']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    contact = request.form['contact']

    # Check if email already exists in Organization table
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Organization WHERE email = ?", (email,))
        existing_org = cursor.fetchone()
        
        if existing_org:
            flash("Email already exists! Please use a different email.", "error")
            return redirect(url_for('organisation_signup_page'))
        
        # Insert new organization data into Organization table
        cursor.execute("INSERT INTO Organization (unique_id, name, email, password, contact) VALUES (?, ?, ?, ?, ?)", 
                       (unique_id, name, email, password, contact))
        conn.commit()
    
    flash("Organization signed up successfully!")
    return redirect(url_for('org_dashboard'))  

@app.route('/org_dashboard')
def org_dashboard():
    # Serve the dashboard after successful signup
    return render_template('Module_C/organisation_login_signup/org_dashboard/dashboard.html')

# Define a route for donor login (and similarly for organization login)
@app.route('/donor_login', methods=['POST'])
def donor_login():
    email = request.form['email']
    password = request.form['password']

    # Verify donor credentials
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Donor WHERE email = ? AND password = ?", (email, password))
        donor = cursor.fetchone()

        if donor:
            flash("Login successful!")
            return redirect(url_for('donor_dashboard'))  # Redirect to donor dashboard upon login
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('donor_signup_page'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

import bcrypt
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import sqlite3
# import google.generativeai as genai  # Import Google Generative AI modu
app = Flask(__name__, template_folder='templates', static_folder='templates')
app.secret_key = "your_secret_key"  # Required for flash messages

# Configure Gemini API with the correct key
# genai.configure(api_key="AIzaSyD1h8zNaWMAVk5VMDkyNZL2ByCaJwOGX9Y")

# Function to generate FAQ responses using the Gemini model
# def generate_faq_response(query):
#     try:
#         prompt = f"Answer the following FAQ: {query}"
#         response = genai.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# Initialize SQLite Database
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        # Create tables if they don't exist
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
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Request (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            campaign_name TEXT NOT NULL,
                            additional_requirements TEXT NOT NULL,
                            item TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            approx_price REAL NOT NULL)''')

        conn.commit()

# Initialize database
init_db()

@app.route('/')
def landing_page():
    return render_template('landing_page/index.html')

# Donor signup page
@app.route('/donor_signup_page')
def donor_signup_page():
    return render_template('Module_A/Donor_dashboard/signup.html')

# Donor Dashboard 
@app.route('/donor_dashboard_page')
def donor_dashboard_page():
    return render_template('Module_A/Donor_dashboard/donor_dashboard.html')

# Organization signup page
@app.route('/organisation_signup_page')
def organisation_signup_page():
    return render_template('Module_C/organisation_login_signup/signup.html')

# Organization dashboard page
@app.route('/organisation_dashboard_page')
def organisation_dashboard_page():
    return render_template('Module_C/organisation_login_signup/org_dashboard/dashboard.html')

# Handle Donor signup form submission
@app.route('/donor_signup', methods=['POST'])
def donor_signup():
    donor_name = request.form['name']
    donor_email = request.form['loginEmail']
    donor_password = request.form['password']
    donor_contact = request.form['contact']

    # Check if email already exists in Donor table
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Donor WHERE email = ?", (donor_email,))
        existing_donor = cursor.fetchone()
        
        if existing_donor:
            flash("Email already exists! Please use a different email.", "error")
            return redirect(url_for('donor_signup_page'))
        
        # Insert new donor data into Donor table
        cursor.execute("INSERT INTO Donor (name, email, password, contact) VALUES (?, ?, ?, ?)", 
                       (donor_name, donor_email, donor_password, donor_contact))
        conn.commit()
    
        flash("Donor signed up successfully!")
        return redirect(url_for('donor_dashboard_page'))

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
        
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert new organization data into Organization table
        cursor.execute("INSERT INTO Organization (unique_id, name, email, password, contact) VALUES (?, ?, ?, ?, ?)", 
                       (unique_id, name, email, hashed_password, contact))
        conn.commit()
    
        flash("Organization signed up successfully!")
        return redirect(url_for('organisation_dashboard_page')) 

# Handle Donor login
@app.route('/donor_login', methods=['POST'])
def donor_login():
    donor_login_email = request.form['loginEmail']
    donor_login_password = request.form['loginPassword']

    # Verify donor credentials
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Donor WHERE email = ? AND password = ?", (donor_login_email, donor_login_password))
        donor = cursor.fetchone()

        if donor:
            flash("Login successful!")
            return redirect(url_for('donor_dashboard_page'))  # Redirect to donor dashboard upon login
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('donor_signup_page'))
        
# Handle Organization login
@app.route('/org_login', methods=['POST'])
def org_login():
    org_login_email = request.form['loginEmail']
    org_login_password = request.form['loginPassword']

    # Verify organization credentials
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Organization WHERE email = ? AND password = ?", (org_login_email, org_login_password))
        org = cursor.fetchone()

        if org:
            flash("Login successful!")
            return redirect(url_for('organisation_dashboard_page'))  # Redirect to organization dashboard upon login
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('organisation_dashboard_page'))
        
# Handle Request form submission
@app.route('/submit-request', methods=['POST'])
def submit_request():
    campaign_name = request.form.get('ngo-name')
    additional_requirements = request.form.get('reason')
    item = request.form.get('item')
    quantity = request.form.get('quantity')
    approx_price = request.form.get('approx-price')

    # Debug: Print received data
    print(f"Form Data Received: campaign_name={campaign_name}, additional_requirements={additional_requirements}, item={item}, quantity={quantity}, approx_price={approx_price}")

    # Insert form data into Request table
    try:
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Request (campaign_name, additional_requirements, item, quantity, approx_price)
                              VALUES (?, ?, ?, ?, ?)''', 
                           (campaign_name, additional_requirements, item, quantity, approx_price))
            conn.commit()
        flash("Request submitted successfully!")
    except Exception as e:
        print(f"Error inserting into database: {e}")
        flash(f"An error occurred: {str(e)}", "error")

    return redirect(url_for('organisation_dashboard_page'))

# Fetch campaigns for display
@app.route('/get_campaigns', methods=['GET'])
def get_campaigns():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Request")
        campaigns = cursor.fetchall()
        return jsonify([dict(campaign) for campaign in campaigns])

# Chatbot API for FAQ
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({'error': 'No query provided'}), 400

        # Generate response using the Gemini API
        response = generate_faq_response(user_query)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

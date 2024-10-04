from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='templates')



@app.route('/')
def landing_page():
    # Serve landing_page/index.html from the 'landing_page' folder
    return render_template('landing_page/index.html')

# Define a route for the donor signup page
@app.route('/donor_signup_page')
def donor_signup_page():
    # Serve Module_A/Donor_dashboard/signup.html
    return render_template('templates/Module_A/Donor_dashboard/signup.html')

# Define a route for the organisation signup page
@app.route('/organisation_signup_page')
def organisation_signup_page():
    # Serve Module_C/organisation_login_signup/signup.html
    return render_template('templates/Module_C/organisation_login_signup/signup.html')

# Example route for handling donor signup form submission
@app.route('/donor_signup', methods=['POST'])
def donor_signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    contact = request.form['contact']
    print(f'Donor Signed Up: {name}, {email}, {contact}')
    return redirect(url_for('landing_page'))

# Example route for handling organisation signup form submission
@app.route('/organisation_signup', methods=['POST'])
def organisation_signup():
    unique_id = request.form['uniqueId']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    contact = request.form['contact']
    print(f'Organization Signed Up: {unique_id}, {name}, {email}, {contact}')
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

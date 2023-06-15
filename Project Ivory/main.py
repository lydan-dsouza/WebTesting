from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for demonstration purposes
USERS = {
    'admin': 'admin123',
    'user': 'password123'
}

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Save the user's registration details in the database or any other storage mechanism
        USERS[username] = password
        
        # Redirect to the login page after successful registration
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate the user's credentials from the database or any other storage mechanism
        if username in USERS and USERS[username] == password:
            # If the credentials are valid, set the user's session
            session['username'] = username
            return redirect(url_for('generate_report'))
        
        # If the credentials are invalid, show an error message
        error_message = 'Invalid username or password. Please try again.'
        return render_template('login.html', error_message=error_message)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the user's session and redirect to the login page
    session.clear()
    return redirect(url_for('login'))

@app.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        website_link = request.form['website_link']
        
        # Perform report generation logic here based on the provided website link
        # For demonstration purposes, let's assume a simple success message is displayed
        success_message = f'Report generated for website: {website_link}'
        return render_template('generate_report.html', success_message=success_message)
    
    return render_template('generate_report.html')

@app.route('/report')
def report():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    # Retrieve the report for the currently logged-in user from the database or any other storage mechanism
    # For demonstration purposes, let's assume a dummy report data
    report_data = {
        'title': 'Sample Report',
        'content': 'This is a sample report generated for the user: ' + username
    }
    return render_template('report.html', report_data=report_data)

if __name__ == '__main__':
    app.run(debug=True)


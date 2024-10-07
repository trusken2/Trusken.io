from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime


app = Flask(__name__)

# Secret key for flash messages (required for form handling)
app.config['SECRET_KEY'] = 'your_secret_key_here'


# Home Route
@app.route('/home/')
@app.route('/')
def home():
    return render_template('home.html', year=datetime.now().year)


# About Route
@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)


# Services Route
@app.route('/product')
def product():
    return render_template('product.html', year=datetime.now().year)


# Contact Route (with GET and POST methods)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form inputs
        if not name or not email or not message:
            flash("All fields are required!", "error")
            return redirect(url_for('contact'))  # Avoid recursion errors by not redirecting to itself continuously

        # Optionally: Logic to send emails or store data can be added here

        flash("Thank you for contacting us!", "success")
        return redirect(url_for('home'))  # Redirect to a valid route after processing

    # Render the contact form
    return render_template('contact.html', year=datetime.now().year)


# Privacy Policy Route
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', year=datetime.now().year)


# Blog Route
#@app.route('/blog')
#def blog():
    #return render_template('blog.html', year=datetime.now().year)


# Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', year=datetime.now().year), 404


# Custom 500 Error Handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', year=datetime.now().year), 500


# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)

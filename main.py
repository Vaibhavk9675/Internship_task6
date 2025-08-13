from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    
    # Append to a text file
    with open("contacts.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Name: {name} | Email: {email} | Phone: {phone} | Message: {message}\n")
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

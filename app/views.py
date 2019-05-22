from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    message = 'Welcome to your favorite News Channel'
    return render_template('index.html',message=message)




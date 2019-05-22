from flask import render_template
from app import app

# Views
@app.route('/') #homepage route
def index():
    message = 'Welcome to your favorite News Channel'
    title = 'Taarifa za Habari'
    return render_template('index.html', message=message, title=title)



@app.route('/news_article') #news article route
def news():
    
    return render_template('news_article.html')
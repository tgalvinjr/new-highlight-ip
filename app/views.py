from flask import render_template
from app import app
from .request import get_news
from .models.news import News

# Views
@app.route('/') #homepage route
def index():
    message = 'Welcome to your favorite News Channel'
    title = 'Taarifa za Habari'
    
    current_news = get_news() 
    return render_template('index.html', message=message, title=title, current_news=current_news)



@app.route('/news_article') #news article route
def news():
    
    return render_template('news_article.html') 
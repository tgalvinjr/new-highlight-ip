from app import app
import urllib.request,json
from .models import news
News = news.News
Articles = news.Articles

news_url = None

api_key = app.config ['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
articles_base_url = app.config["ARTICLES_API_BASE_URL"]


def get_news():
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            # print(news_results)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        

        news_object = News(id, name, description, url)

        

        news_results.append(news_object)
        # print(news_results)

    return news_results

def get_articles(id):
    get_articles_url = articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
           

    return articles_results

def process_articles_results(articles_list):
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        author = articles_item.get('author')
        publishedAt = articles_item.get('publishedAt')
        urlToImage = articles_item.get('urlToImage')
        content = articles_item.get('content')
        description = articles_item.get('description')
        url = articles_item.get('url')
        

        articles_object = Articles(title, author, urlToImage, publishedAt, content, description, url)

        

        articles_results.append(articles_object)
       

    return articles_results

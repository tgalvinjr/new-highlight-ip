from app import app
import urllib.request,json
from .models import news
News = news.News

api_key = app.config ['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]


def get_news():
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            print(news_results)

        return news_results

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        

        news_object =  News(id, name, description, url)

        

        news_results.append(news_object)
        print(news_results)

    return news_results



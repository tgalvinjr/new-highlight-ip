import unittest
from .models import news
News = news.News
Articles = news.Articles
from app.models import News,Articles


class NewsTest (unittest.TestCase):

    def setUp(self):
        self.new_news = News("id", 'name','description', 'url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


class ArticlesTest (unittest.TestCase):

    def setUp(self):
        self.new_article = Articles('author', 'title', 'urlToImage', 'publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))



import unittest
from .models import news
News = news.News


class NewsTest (unittest.TestCase):

    def setUp(self):
        self.new_news = News("id", 'name','description', 'url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


class ArticlesTest (unittest.TestCase):

    def setUp(self):
        self.new_article = Article('author', 'title', 'urlToImage', 'publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

if __name__ == '__main__':
    unittest.main()


class News:
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Articles:
    def __init__(self, author, title, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

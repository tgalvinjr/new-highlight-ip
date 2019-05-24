class News:
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Articles:
    def __init__(self, author, title, urlToImage, publishedAt, content, description, url):
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.description = description
        self.url = url
import scrapy


class MostWatchedMoviesSpider(scrapy.Spider):
    name = "most_watched_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls053826112/"]

    def parse(self, response):
        pass

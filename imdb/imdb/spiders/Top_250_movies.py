import scrapy


class Top250MoviesSpider(scrapy.Spider):
    name = "Top_250_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        movies = response.css()

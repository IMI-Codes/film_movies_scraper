import scrapy


class A2022MoviesSpider(scrapy.Spider):
    name = "20_22_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls565690655/"]

    def parse(self, response):
        pass

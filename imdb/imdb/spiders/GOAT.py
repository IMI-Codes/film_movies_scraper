import scrapy


class GoatSpider(scrapy.Spider):
    name = "GOAT"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls055592025/"]

    def parse(self, response):
        pass

import scrapy


class Last25YearsSpider(scrapy.Spider):
    name = "last_25_years"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls000562323/"]

    def parse(self, response):
        pass

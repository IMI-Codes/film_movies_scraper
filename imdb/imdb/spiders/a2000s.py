import scrapy


class A2000sSpider(scrapy.Spider):
    name = "2000s"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls002065120/"]

    def parse(self, response):
        pass

import scrapy


class YearByYearSpider(scrapy.Spider):
    name = "year_by_year"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls058788200/"]

    def parse(self, response):
        pass

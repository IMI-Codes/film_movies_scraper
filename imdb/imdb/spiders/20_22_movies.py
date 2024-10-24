import scrapy
from imdb.items import _2022_movies

class A2022MoviesSpider(scrapy.Spider):
    name = "20_22_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls565690655/"]

    def parse(self, response): # type: ignore
        movies = response.css("li.ipc-metadata-list-summary-item")
        value = _2022_movies()
        for movie in movies:
            value["name"] = movie.css("h3.ipc-title__text ::text").get()
            value["meta_Data"] = movie.css(".dli-title-metadata-item ::text").getall()
            value["rating"] = movie.css("span.ipc-rating-star--rating ::text").get()
            value["plot"] = movie.css(".ipc-html-content-inner-div ::text").get()
            yield value
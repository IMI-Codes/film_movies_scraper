import scrapy
from imdb.items import Most_watched_Item

class MostWatchedMoviesSpider(scrapy.Spider):
    name = "most_watched_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/list/ls053826112/","https://www.imdb.com/list/ls058788200/","https://www.imdb.com/list/ls565690655/","https://www.imdb.com/list/ls002065120/","https://www.imdb.com/list/ls055592025/","https://www.imdb.com/list/ls000562323/"]

    def parse(self, response): # type: ignore
        for url in self.start_urls:
            movies = response.css("li.ipc-metadata-list-summary-item")
            value = Most_watched_Item()
            for movie in movies:
                value["name"] = movie.css("h3.ipc-title__text ::text").get()
                value["meta_Data"] = movie.css(".dli-title-metadata-item ::text").getall()
                value["rating"] = movie.css("span.ipc-rating-star--rating ::text").get()
                value["plot"] = movie.css(".ipc-html-content-inner-div ::text").get()
                yield value
        
        
        #name = h3.ipc-title__text
        #metadata = .dli-title-metadata-item ::text .getall()
        #rating = span.ipc-rating-star--rating
        #plot = .ipc-html-content-inner-div
        #imdb\scraped_data

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Most_watched_Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    meta_Data = scrapy.Field()
    rating = scrapy.Field()
    plot = scrapy.Field()
    release_year = scrapy.Field()
    film_length = scrapy.Field()
    age_rating = scrapy.Field()
    occurrence = scrapy.Field()
    

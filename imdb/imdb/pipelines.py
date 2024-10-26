# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # type: ignore
import re

class ImdbPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        name = adapter.get("name")
        pattern = re.compile(r"(\d+).")
        test = pattern.search(name) # type: ignore
        chop_range = test.span()
        start,stop = chop_range
        final_name = name[stop:].strip() # type: ignore
        adapter["name"] = final_name
        
        met_data = adapter.get("meta_Data")
        
        release_year = met_data[0] # type: ignore
        movie_length = met_data[1] # type: ignore
        age_rating = met_data[2]  # type: ignore
        if release_year:
            adapter["release_year"] = release_year
        if movie_length:
            adapter["film_length"] = movie_length
        if age_rating:
            adapter["age_rating"] = age_rating
        return item
class dropMeta:
    def process_item(self,item,spider):
        adapter = ItemAdapter(item)
        #item.__delitem__("meta_Data")
        adapter.__delitem__("meta_Data")
        return item


from scrapy.exceptions import DropItem
class Check_duplicate:
    def __init__(self) -> None:
        self.movie_name = set()
        
    def process_item(self,item,spider):
        adapter = ItemAdapter(item)
        name = adapter.get("name")
        if name in self.movie_name: 
           raise  DropItem(item)
        else:
            self.movie_name.add(name)
        print(self.movie_name)
        return item 
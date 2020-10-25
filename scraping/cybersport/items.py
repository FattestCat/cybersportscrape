# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Post(Item):
    title = Field()
    # content = Field()
    date = Field()
    # tags = Field()
    # comments_count = Field()


class CybersportItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
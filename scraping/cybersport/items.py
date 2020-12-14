# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Post(Item):
    title = Field()
    content = Field()
    date = Field()
    tags = Field()
    # comments_count = Field()

class PostDot(Item):
    title = Field()
    content = Field()
    date = Field()
    tags = Field()

class CybersportItem(Item):
    pass

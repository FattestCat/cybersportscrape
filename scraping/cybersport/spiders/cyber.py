from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector

import json

from .xpaths import *
from ..items import Post
from ..pipelines import (DateChecker,
                        DefaulValueSetter,
                        DataCleaner,
                        WordsNormilizer)
from ..util import print_f

class Cyber(Spider):

    custom_settings = {
        "ITEM_PIPELINES": {
            DateChecker: 90,
            DefaulValueSetter: 100,
            DataCleaner: 200,
            WordsNormilizer: 300,
        }
    }

    count = [0]
    name = 'cyber'
    allower_domains = ['cybersport.ru']

    def start_requests(self):
        yield Request('https://cybersport.ru/news/page/2', callback=self.parse)

    def parse(self, response):
        json_body = json.loads(response.text)
        next_page = json_body.get('nextPageUri', None)
        selector = Selector(text=json_body['list'])
        links = selector.xpath(XPATH_POST_LINK).getall()
        l = len(links)
        for link in links:
            self.count[0] += 1
            yield Request(f'https://cybersport.ru{link}', callback=self.parse_links)

        if next_page and self.count[0] < 81:
            yield Request(f'https://cybersport.ru{next_page}', callback=self.parse)

    def parse_links(self, response):
        item_loader = ItemLoader(item=Post(), response=response)
        item_loader.add_xpath('title', XPATH_POST_TITLE)
        item_loader.add_xpath('date', XPATH_POST_DATE)
        item_loader.add_xpath('content', XPATH_POST_CONTENT)
        item_loader.add_xpath('tags', XPATH_POST_TAGS)
        print_f('PARSE LINKS')
        yield item_loader.load_item()

from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector

from .xpaths import *
from ..items import PostDot
from ..pipelines import (
        DateChecker,
        DefaultValueSetter,
        DataCleaner,
        WordsNormilizer,
        DataSenderForPostDot,
        )
from ..util import print_f

class CyberDot(Spider):
    
    custom_settings = {
            "ITEM_PIPELINES": {
                # DateChecker: 90,
                DefaultValueSetter: 100,
                DataCleaner: 200,
                DataSenderForPostDot: 250,
                # WordsNormilizer: 300,
            },
            # "ROBOTSTXT_OBEY" : False
    }

    count=[0]
    name = 'cyberdot'
    allowed_domains = ['cyber.sports.ru']

    def start_requests(self):
        print_f('STARTING')
        yield Request('https://cyber.sports.ru/news/', callback=self.parse)


    def parse(self, response):
        links = response.xpath(XPATH_POST_LINK_DOT).getall()
        next_page = response.xpath(XPATH_POST_NEXT_PAGE_DOT).getall()
        print(links)
        print(next_page)

        for link in links:
            self.count[0] += 1
            yield Request(f'https://cyber.sports.ru{link}', callback=self.parse_links)

        if self.count[0] < 160 and next_page:
            nxt = next_page[0]
            yield Request(f'https://cyber.sports.ru/news/{nxt}', callback=self.parse)


    def parse_links(self, response):
        item_loader = ItemLoader(item=PostDot(), response=response)
        item_loader.add_xpath('title', XPATH_POST_TITLE_DOT)
        item_loader.add_xpath('date', XPATH_POST_DATE_DOT)
        item_loader.add_xpath('content', XPATH_POST_CONTENT_DOT)
        item_loader.add_xpath('tags', XPATH_POST_TAGS_DOT)
        print_f('LOADING ITEMS')
        yield item_loader.load_item()

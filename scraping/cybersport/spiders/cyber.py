from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector

import json

from .xpaths import *
from ..items import Post



class Cyber(Spider):
    custom_settings = {
        # ADD PIPLENES
    }
    count = [0]
    name = 'cyber'
    allower_domains = ['cybersport.ru']

    def start_requests(self):
        yield Request('https://cybersport.ru/news/page/2', callback=self.parse)

    def parse(self,response):
        json_body = json.loads(response.text)
        has_next = json_body.get('nextPageUri', None)
        selector = Selector(text=json_body['list'])
        links = selector.xpath(XPATH_POST_LINK).getall()
        l = len(links)
        print(f':::::::::::::::::::::::::::::::LENTH OF LiST OF LINKS = {l} :::::::::::::::::::::::::::::')
        for link in links:
            self.count[0]+=1
            yield Request(f'https://cybersport.ru{link}', callback=self.parse_linst)
        
        if has_next and self.count[0]<100:
            yield Request(f'https://cybersport.ru{has_next}',callback=self.parse)
        print(f':::::::::::::::{has_next}:::::::::::::::::::::')
        
    def parse_linst(self, response):
        item_loader = ItemLoader(item=Post, response=response)
        pass

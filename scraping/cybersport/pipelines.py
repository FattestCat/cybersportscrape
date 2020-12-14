
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

import pymorphy2
from datetime import datetime
import requests
import os

from .util import print_f

morph = pymorphy2.MorphAnalyzer()

USER = os.environ.get('CYBER_DATA_USER')
PASS = os.environ.get('CYBER_DATA_PASS')

auth = (USER, PASS)
url_for_post = 'http://127.0.0.1:3333/postdata/'
url_for_post_dot = 'http://127.0.0.1:3333/postdatadot/'

# date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')


class DateChecker:
    def process_item(self, item, spide):
        try:
            date_str = item['date'][0]
            print_f(item['date'][0])
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        except KeyError:
            raise DropItem('Post has no date')
        return item


class DefaultValueSetter:
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, None)
        print_f('DefaultValueSetter')
        return item


class DataCleaner:
    def process_item(self, item, spider):
        print_f('DataCleaner')
        print_f(f'{item.fields}')
        for field in item.fields:
            if not item[field]:
                print_f('CHEKINKG FIELDS')
                print(item)
                raise DropItem(f':::::::::Missings {field} field:::::::::::')
        print_f('WE PASSED RAISE')
        item['content'] = ' '.join(item['content'])
        adaper = ItemAdapter(item)
        print_f(f'{USER} {PASS}')
        # response = requests.post(url, data=adaper.asdict(), auth=auth)
        # print_f('ADAPTER ASDICT')
        # print(response)
        return item

class DataSenderForPost:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print_f('adapter as dict')
        response = requests.post(url_for_post, data=adapter.asdict(), auth=auth)
        print(response)

class DataSenderForPostDot:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print_f('adapter as dict')
        response = requests.post(url_for_post_dot, data=adapter.asdict(), auth=auth)
        print(response)

class WordsNormilizer:
    def process_item(self, item, spider):
        print_f('WORD NORMALIZER')
        return item

    def open_spider(self, spider):
        print_f('WN CONNECTED')

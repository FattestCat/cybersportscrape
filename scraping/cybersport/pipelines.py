# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

import pymorphy2
from datetime import datetime

from .util import print_f

morph = pymorphy2.MorphAnalyzer()


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

class DefaulValueSetter:
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, None)
        print_f('DefaulValueSetter')
        return item


class DataCleaner:
    def process_item(self, item, spider):
        print_f('DataCleaner')
        print_f(f'{item.fields}')
        for field in item.fields:
            if not item[field]:
                print_f('CHEKINKG FIELDS')
                raise DropItem(f':::::::::Missings {field} field:::::::::::')
        print_f('WE PASSED RAISE')
        return item


class WordsNormilizer:
    def process_item(self, item, spider):
        print_f('WORD NORMALIZER')
        return item

    def open_spider(self, spider):
        print_f('WN CONNECTED')

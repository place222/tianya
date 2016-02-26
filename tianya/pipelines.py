# -*- coding: utf-8 -*-
"""
    pipeLines是对Spider收集之后对Item的处理
    一般应用:
        清理html数据
        验证爬取得数据
        查重
        将爬取结果保存到数据库等
    DropItem的异常会丢弃Item
"""
from scrapy.exceptions import DropItem
import scrapy

class TianyaPipeline(object):
    """
    验证
    """

    def process_item(self, item, spider):
        if item:
            if len(item['title']) > 0:
                item['title'] = item['title'][0].lstrip().rstrip()
                print item['title']
        else:
            raise DropItem('this is Item title is empty %s' % item)
        return item

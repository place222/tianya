# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tianya.items import TianyaItem

class TianyaSpiderSpider(scrapy.Spider):
    name = "tianya_spider"
    allowed_domains = ["tianya.cn"]
    start_urls = (
        'http://bbs.tianya.cn/list-333-1.shtml',
    )

    def parse(self, response):
        """

        :param response:
        :return:
        """
        # 这个是一般选择器分析填充Item
        selector = Selector(response)
        trs = selector.xpath('//table[@class="tab-bbs-list tab-bbs-list-2"]//tr')
        for tr in trs:
            item = TianyaItem()
            item['title'] = tr.xpath('.//a[1]/text()').extract()
            item['author'] = tr.xpath('.//a[2]/text()').extract()
            item['clicktime'] = tr.xpath('.//td[3]/text()').extract()
            item['backtime'] = tr.xpath('.//td[4]/text()').extract()
            item['backdate'] = tr.xpath('.//td[5]/text()').extract()
            yield item
        # 这个是采用ItemLoader
        # l = ItemLoader(item = TianyaItem(),response = response)
        # l.add_xpath('title','.//')
        # yield l.load_item()
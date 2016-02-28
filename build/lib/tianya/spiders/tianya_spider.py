# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector,SelectorList
from tianya.items import TianyaItem
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from scrapy.log import INFO

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
            item['title'] = tr.xpath('.//td[1]/a/text()').extract()
            item['author'] = tr.xpath('.//td[2]/a/text()').extract()
            item['clicktime'] = tr.xpath('.//td[3]/text()').extract()
            item['backtime'] = tr.xpath('.//td[4]/text()').extract()
            item['backdate'] = tr.xpath('.//td[5]/text()').extract()
            yield item

        # 构建下一页的link
        # links = selector.xpath('//div[@class="links"]//a/@href[last()]').extract()
        # if isinstance(links,(list,)) and len(links) > 0:
        #     link = 'http://bbs.tianya.cn'+links[-1]
        #     yield Request(link,callback=self.parse)
        # else:
            self.log(u'已经到头了!', level=INFO)



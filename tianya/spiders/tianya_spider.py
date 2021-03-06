# -*- coding: utf-8 -*-
"""

"""

import scrapy
from scrapy.selector import Selector,SelectorList
from tianya.items import TianyaItem
from scrapy.http import Request
from scrapy.log import INFO
from scrapy.spiders.crawl import CrawlSpider


class TianyaSpiderSpider(CrawlSpider):

    name = "tianya_spider"
    allowed_domains = ["tianya.cn"]
    start_urls = (
        'http://bbs.tianya.cn/list-333-1.shtml',
    )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TianyaSpiderSpider,cls).from_crawler(crawler,*args,**kwargs)
        spider.stats = crawler.stats
        return spider

    def start_requests(self):
        """

        :return:
        """
        self.log('开始从start_urls构建开始地址 构建Request对象')
        return super(TianyaSpiderSpider,self).start_requests()

    def make_requests_from_url(self,url):
        """

        :param url:
        :return:
        """
        self.log("make_requests_from_url!")
        return super(TianyaSpiderSpider,self).make_requests_from_url(url)

    def parse(self, response):
        """

        :param response:
        :return:
        """
        # 这个是一般选择器分析填充Item
        selector = Selector(response)
        trs = selector.xpath('//table[@class="tab-bbs-list tab-bbs-list-2"]//tr')
        self.stats.set_value('liuyang','liuyang')

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
        #     self.log(u'已经到头了!', level=INFO)



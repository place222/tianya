# -*- coding: utf-8 -*-
import scrapy


class TianyaTaiwanSpiderSpider(scrapy.Spider):
    name = "tianya_taiwan_spider"
    allowed_domains = ["tianya.cn"]
    start_urls = (
        'http://www.tianya.cn/',
    )

    def parse(self, response):
        pass

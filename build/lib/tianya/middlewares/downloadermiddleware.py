# -*-coding=utf-8-*-
"""
监控下载器的链接等等信息
"""

from scrapy.http import Response,Request

class MyDownLoaderMiddleware(object):
    """

    """
    def __init__(self,str):
        self.str = str

    @classmethod
    def from_crawler(cls,crawler):
        str = crawler.settings.get('BOT_NAME')
        return cls(str)

    def process_request(self,request,spider):
        """
        当每个request通过下载中间件 被调用
        :param request: Request
        :param spider:
        :return:None对象Response对象Request对象或者raise IgnoreRequest

        """
        print self.str
        return Response(request.url,body='123')

    # def process_response(self,response,spider):
    #     pass

    # def process_exception(self,request,exception,spider):
    #     pass
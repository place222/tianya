# -*-coding:utf-8-*-

"""

"""
class MyCustomSpiderMiddleware(object):
    """

    """
    #
    # def process_spider_input(self,response,spider):
    #     """
    #
    #     :param response:
    #     :param spider:
    #     :return:
    #     """
    #     print '111111111111111111111111111111111111111111111111111111111111111111'
    #     pass
    #
    def process_spider_output(self, response, result, spider):
        print '------------------------process_spider_output----------------------------'
        return (r for r in result)

    # def process_spider_exception(self,exception,spider):
    #     """
    #
    #     :param exception:
    #     :param spider:
    #     :return:
    #     """
    #     pass
    #
    # def process_start_requests(self,start_requests,spider):
    #     """
    #
    #     :param start_requests:
    #     :param spider:
    #     :return:
    #     """
    #     return

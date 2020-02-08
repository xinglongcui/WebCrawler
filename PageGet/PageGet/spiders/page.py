# -*- coding: utf-8 -*-
import scrapy


class PageSpider(scrapy.Spider):
    name = 'page'
    allowed_domains = ['10jqka']
    start_urls = [
                  'http://quote.eastmoney.com/center/boardlist.html#industry_board',
                  ]
#    allowed_domains = ['jd.com']
#    start_urls = ['http://jd.com']

    def parse(self, response):
        tmp_page_file = response.url.split("//")[1]
        #page_file = tmp_page_file.split("/")[0] + ".html"
        page_file = tmp_page_file.replace("/", "_") + ".html"
        with open (page_file, 'wb') as f:
            f.write(response.body)

        self.log("page file is %s" %page_file)

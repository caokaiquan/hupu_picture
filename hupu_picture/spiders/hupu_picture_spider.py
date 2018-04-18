# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from scrapy.http import Request
from ..items import HupuPictureItem


class HupuPictureSpiderSpider(scrapy.Spider):
    name = 'hupu_picture_spider'
    allowed_domains = ['hupu.com']
    start_urls = ['https://bbs.hupu.com/selfie']

    def parse(self, response):
        jpy = PyQuery(response.text)
        urls_item = jpy('#ajaxtable > div.show-list > ul > li').items()


        for url in urls_item:
            yield response.follow(url('div.titlelink.box > a').attr('href'), callback=self.picture_parse, errback=self.error_back)

        # 翻页
        url_list = ['https://bbs.hupu.com/selfie-{}'.format(i) for i in range(2, 11)]
        for k in url_list:
            yield Request(k, callback=self.parse, errback=self.error_back)


    def picture_parse(self,response):
        pp = PyQuery(response.text)
        item = HupuPictureItem()
        img = pp('#tpc > div > div.floor_box > table.case > tbody > tr > td > div.quote-content img').items()
        if img is not None:
            for i in img:
                item['picture'] = i.attr('src').split('?')[0]
                item['picture_name'] = response.url
                yield item



    def error_back(self,e):
        _ = self
        print(e)























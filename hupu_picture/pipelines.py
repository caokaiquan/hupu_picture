# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import random
import os
class HupuPicturePipeline(object):
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
        '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
    ]
    os.makedirs('image_hupu')
    def process_item(self, item, spider):
        id = item['picture'].split('_')[-1]
        ua = random.choice(self.ua_list)
        header = {'User-Agent': ua}
        self.file = open('./image_hupu/'+'{}'.format(id),'wb')
        picture = requests.get(item['picture'],headers = header)
        self.file.write(picture.content)
        self.file.close()
        return item























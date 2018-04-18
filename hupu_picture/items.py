# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuPictureItem(scrapy.Item):
    picture = scrapy.Field()
    picture_name = scrapy.Field()


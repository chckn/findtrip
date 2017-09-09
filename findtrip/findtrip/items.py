# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindtripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site = scrapy.Field()
    flight = scrapy.Field()

    dep_city=scrapy.Field()
    arr_city=scrapy.Field()
    via_city=scrapy.Field()
    flight_date=scrapy.Field()
    
    dep_time = scrapy.Field()
    arr_time = scrapy.Field()

#    airports = scrapy.Field()
#   passtime = scrapy.Field()
    price = scrapy.Field()

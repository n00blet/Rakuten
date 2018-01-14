# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst


class RakutenItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    handbag_price = Field(output_processor=TakeFirst())
    handbag_url = Field(output_processor=TakeFirst())
    handbag_brand = Field(output_processor=TakeFirst())
    handbag_image_urls = Field(output_processor=TakeFirst())

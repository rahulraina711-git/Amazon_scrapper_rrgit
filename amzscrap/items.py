# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmzscrapItem(scrapy.Item):
    # define the fields for your item here like:
    item_name = scrapy.Field()
    item_price = scrapy.Field()
    item_rating = scrapy.Field()
    item_image = scrapy.Field()
    pass

import scrapy

class NudityImages(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()

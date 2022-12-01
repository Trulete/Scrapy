# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectoImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ImdbItem(scrapy.Item):
    
    titulo = scrapy.Field()
    popularidad = scrapy.Field()
    userrev = scrapy.Field()
    critrev = scrapy.Field()
    direccion = scrapy.Field()
    reparto = scrapy.Field()


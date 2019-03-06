# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySakuraItem(scrapy.Item):
    # define the fields for your item here like:

    cover = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    time = scrapy.Field()
    area = scrapy.Field()
    type = scrapy.Field()
    tag = scrapy.Field()
    presentation = scrapy.Field()

    # def get_insert_sql(self):
    #     insert_sql = "INSERT INTO info(name,score,time,area,type,tag,presentation) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    #     params = (
    #         self['name'], self['score'], self['time'], self['area'],
    #         self['type'], self['tag'], self['presentation']
    #     )
    #     return insert_sql, params
    def get_insert_sql(self):
        insert_sql = "INSERT INTO info(name,score,time,area,type,tag,presentation) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        params = (
            self['name'], self['score'], self['time'], self['area'],
            str(self['type']), str(self['tag']), str(self['presentation'])
        )
        return insert_sql, params


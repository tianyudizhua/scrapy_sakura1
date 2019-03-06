# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors


class ScrapySakuraPipeline(object):
    def process_item(self, item, spider):
        return item


class Imagespiderpipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['cover'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None):
        filename = re.sub(r'[\\*|?"<>:/]', '', request.meta['name']) + '.jpg'
        return filename


class MysqlTwistedPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    # 从setting中读取数据
    def from_settings(cls, settings):
        db_params = dict(
            db=settings.get('MYSQL_DB_NAME'),
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWORD'),
            charset=settings.get('MYSQL_CHARSET'),
            use_unicode=True,
            # 设置游标类型
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool)

    def process_item(self, item, spider):
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, item)
        # 如果sql执行发送错误自动回调addErrBack()函数
        query.addErrback(self.handle_error, item, spider)

    def insert_into(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        print(failure)

    def data_list(self):
        pass

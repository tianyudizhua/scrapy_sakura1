# -*- coding: utf-8 -*-
import scrapy
from scrapy_sakura.items import ScrapySakuraItem


class SakuraCartoonSpider(scrapy.Spider):
    name = 'sakura_cartoon'
    allowed_domains = ['www.yhdm.tv']
    # start_urls = ['http://www.yhdm.tv/japan/',
    #               'http://www.yhdm.tv/china/',
    #               'http://www.yhdm.tv/american/', ]
    start_urls = ['http://www.yhdm.tv/japan/']

    def parse(self, response):
        detail_url = response.xpath('//div[@class="lpic"]/ul/li/a/@href').extract()
        next_page_url = response.xpath('//div[@class="pages"]/a/@href').extract()[-1]
        for d in detail_url:
            yield scrapy.Request(response.urljoin(d), callback=self.detail_parse)
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    #
    def detail_parse(self, response):
        item = ScrapySakuraItem()
        item['cover'] = response.xpath('//div[@class="thumb l"]/img/@src').extract_first()
        item['name'] = response.xpath('//div[@class="rate r"]/h1//text()').extract_first()
        item['score'] = response.xpath('//div[@class="score"]/em//text()').extract_first()
        item['time'] = response.xpath('//div[@class="sinfo"]/span[1]//text()').extract()[1] + response.xpath('//div[@class="sinfo"]/span[1]//text()').extract()[2]
        item['area'] = response.xpath('//div[@class="sinfo"]/span[2]/a//text()').extract()[0]
        item['type'] = response.xpath('//div[@class="sinfo"]/span[3]/a//text()').extract()
        item['tag'] = response.xpath('//div[@class="sinfo"]/span[5]/a//text()').extract()
        item['presentation'] = response.xpath('//div[@class="info"]//text()').extract_first()
        print(item)
        yield item

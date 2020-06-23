# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from liuli.items import LiuliItem


class DongmanSpider(CrawlSpider):
    name = 'dongman'
    allowed_domains = ['llss.live']
    start_urls = ['http://llss.live/wp/']

    rules = (
        Rule(LinkExtractor(allow='http://llss.live/wp/category/all/anime/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = LiuliItem()
        item['urls'] = response.xpath('//div[@id="content"]//img/@src').extract()
        item['title'] = response.xpath('//div[@id="content"]//h1/a/text()').extract()
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class LiuliPipeline(object):
    def process_item(self, item, spider):
        return item


class DongmanPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        title = item['title']
        urls = item['urls']
        for url in zip(title, urls):
            yield scrapy.Request(url[1], meta={'item': url[0]})

    def file_path(self, request, response=None, info=None):
        title = request.meta['item']
        return 'full/{0}.jpg'.format(title)

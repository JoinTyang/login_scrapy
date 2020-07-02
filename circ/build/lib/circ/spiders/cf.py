# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['cbirc.gov.cn']
    start_urls = ['http://www.cbirc.gov.cn/cn/view/pages/ItemList.html']

    rules = (
        # Rule(LinkExtractor(allow=r'/static/data/DocInfo/SelectByDocId/data_docId=\d+\.json'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/cn/view/pages/ItemDetail.html?docId=\d+\&itemId=4115&generaltype=9'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        # item["title"] = json.loads(response.body.decode())["data"]["docTitle"]
        item["title"] = response.xpath("//div")
        print("item")
        print(item)
        # return item

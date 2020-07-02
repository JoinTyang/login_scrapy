# -*- coding: utf-8 -*-
import re

import scrapy


class LoginTestSpider(scrapy.Spider):
    name = 'login_test'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com']

    def start_requests(self):
        cookies = "_octo=GH1.1.1609086178.1579047893; _ga=GA1.2.146916328.1579047896; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=JoinTyang; _gat=1"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )
    def parse(self, response):
        print("first")
        print(re.findall("JoinTyang",response.body.decode()))
        yield scrapy.Request(
            "https://github.com/JoinTyang",
            callback=self.parse_detail
        )

    def parse_detail(self,response):
        print(re.findall("JoinTyang", response.body.decode()))
        # print(dir(response))
        item={"name":"yt"}
        yield item
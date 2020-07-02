# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # print(response.body)
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        # ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        print(response.xpath("//input[@name='ga_id']/@value"))
        post_data = dict(
            login="JoinTyang",
            password="15809930487y",
            authenticity_token=authenticity_token,
            commit=commit,
            # ga_id=ga_id,
            timestamp=timestamp,
            timestamp_secret=timestamp_secret
        )
        print(post_data)
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        print("ddddd")
        with open("2.html",'wb') as f:
            f.write(response.body)
        print(response.xpath("//input"))
        # print(response.xpath("//div"))
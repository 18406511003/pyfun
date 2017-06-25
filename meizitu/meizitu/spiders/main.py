#user:Tooooooooooo
# -*- coding:utf-8 -*-
import scrapy
from meizitu.items import MeizituItem
class Meizituspider(scrapy.Spider):
    name = "meizitu"

    start_urls = [
        'http://www.tooopen.com/img/87.aspx',
    ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//*[@class="cell first-cell"]')
        for site in sites:
            item = MeizituItem()
            title = site.xpath('a/@title').extract()
            pic_url = site.xpath('a[1]/img/@src').extract()
            item['title'] = [t.encode('utf-8') for t in title]
            item['pic_url'] = pic_url
            yield item
            urls = sel.xpath('//*[@class="page-nav"]/a/@href').extract()
            for url in urls:
                print url
                url = "http://www.tooopen.com"+url
                print url
                yield scrapy.http.Request(url,callback=self.parse)
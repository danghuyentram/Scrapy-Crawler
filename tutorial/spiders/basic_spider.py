import scrapy
import json


class BasicSpider(scrapy.Spider):
    name = "basic"
    start_urls = [
        'https://scrapingclub.com/exercise/detail_basic/'
    ]

    file_name = 'data/basic_spider.json'

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        i = 0
        card = response.css('div.card.mt-4.my-4')
        body = card.css('div.card-body')
        obj = {
            'title': body.css('h3.card-title::text').get(),
            'price': body.css('h4::text').get(),
            'decription': body.css('p.card-text::text').get()
        }

        f = open(self.file_name, "w")
        f.write(json.dumps(obj))
        f.close()
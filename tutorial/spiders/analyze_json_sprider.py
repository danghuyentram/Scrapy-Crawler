import scrapy
import json
import re


class AnalyzeJsonSpider(scrapy.Spider):
    name = "analyzejson"
    start_urls = [
        'https://scrapingclub.com/exercise/detail_json/'
    ]

    file_name = 'data/analyze_json_spider.json'

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        data = re.findall("var obj =(.+?);\n", response.body.decode("utf-8"), re.S)
        f = open(self.file_name, "w")
        f.write(json.dumps(data))
        f.close()
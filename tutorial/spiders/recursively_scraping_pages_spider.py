import scrapy
import json


class RecursivelyScrapingPages(scrapy.Spider):
    name = "recursivelyscrapingpages"
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']
    allowed_domains = ['scrapingclub.com/exercise/list_basic/']


    file_name = 'data/recursively_scraping_pages_spider.json'

    def parse(self, response):
        cards = response.xpath("//div[@class='card-body']")
        i = 0
        for card in cards:
            i = i +1
            yield {
                'title': card.xpath("h4//a/text()").extract_first(),
                'price': card.xpath("h5//text()").extract_first(),
            }

        next_page_url = response.xpath("//a[@class='page-link']/@href").extract_first()
        print("next url %s %d", next_page_url, i)
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            print("next page %s", absolute_next_page_url)
            yield scrapy.Request(absolute_next_page_url)

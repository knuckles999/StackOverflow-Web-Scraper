from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem



class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

# name defines the name of the Spider.
# allowed_domains contains the base-URLs for the allowed domains for the spider to crawl.
# start_urls is a list of URLs for the spider to start crawling from. All subsequent URLs will start from the data that the spider downloads from the URLS in start_urls.


    def parse(self,response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
    #we basically tell Scrapy where to start looking for information based on a defined XPath
        
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item 
            #iterating through the `questions` and assigning the `title` and `url` values from the scraped data




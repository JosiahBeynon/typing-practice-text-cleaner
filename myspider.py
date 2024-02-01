import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MyspiderSpider(CrawlSpider):
    name = "myspider"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def start_requests(self):
        with open('G:\My Drive\Programming\Misc\Typing Practice Code Editor\urls.txt') as f:
            urls = f.readlines()
            
        for url in urls[1]:
            url = url.strip() 
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    xpath = '//body//div[contains(@class, "nav-content")]/div/section/div[5]/div/div[contains(@class, "passage-resources")]/section/div[contains(@class, "passage-table")]/div[contains(@class, "passage-cols")]/div[contains(@class, "passage-col-tools")]/div[contains(@class, "passage-col") and contains(@class, "passage-col-mobile") and contains(@class, "version-NIV")]/div[contains(@class, "passage-text")]/div/div/div[@class="std-text"]'
    
    passage_text = response.xpath(xpath).get()
    
    print(passage_text)



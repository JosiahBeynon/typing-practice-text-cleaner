import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MyspiderSpider(CrawlSpider):
    name = "myspider"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]


    # Set the download delay to 1 second
    custom_settings = {
        'DOWNLOAD_DELAY': 3
    }

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def start_requests(self):
        with open(r'G:\My Drive\Programming\Misc\Typing Practice Code Editor\urls.txt') as f:
            urls = f.readlines()

        for url in urls:
            url = url.strip()
            yield scrapy.Request(url=url, callback=self.parse)

        # url = 'https://www.biblegateway.com/passage/?search=John%206&version=NIV'
        # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # XPath to extract the content
        # xpath = "//div[@class='std-text']//text()[normalize-space()]"  # Select all text nodes within the div
        # xpath = """ 
        # //div[@class='std-text']//text()[normalize-space()]
        # [not(parent::sup[@class='crossreference'])]
        # [not(parent::sup[@class='footnote-marker'])]
        # [not(parent::span[@class='versenum'])]
# """
        # xpath = "normalize-space(//div[@class='chapter']//div[@class='version-NIV'])"
        # xpath = "//span[@class='versenum']//text()"
        # xpath = "//sup[@class='versenum']/text()"

        xpath = "//span[@class='chapternum']/following-sibling::text()"
        chapter_text = response.xpath(xpath).getall()


        xpath = "//sup[@class='versenum']/following-sibling::text()"
        passage_text = response.xpath(xpath).getall()

        # Join the list of text with newlines
        passage_text = '\n'.join(passage_text)
        # full_text = '\n'.join([chapter_text, passage_text])
        full_text = chapter_text[0] + passage_text

        # XPpath to get title
        xpath = "string(//div[@class='dropdown-display-text'])"
        title = response.xpath(xpath).get()

        filename = f'G:\My Drive\Programming\Misc\Typing Practice Code Editor\Raw2\{title}.txt'

        # Save the content to a text file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(full_text)

        self.log(f'Saved content to {filename}')

        # yield {'text': passage_text}

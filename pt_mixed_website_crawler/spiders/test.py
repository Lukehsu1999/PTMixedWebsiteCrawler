import scrapy

class NewsSpider(scrapy.Spider):
    name = 'newspider'
    start_urls = ['https://newbloommag.net/category/main/politics/']

    def parse(self, response):
        for title in response.css('.cb-post-title'):
            yield {'title': title.css('::text').get()}

        for excerpt in response.css('.cb-excerpt'):
            yield {'excerpt': excerpt.css('::text').get()}
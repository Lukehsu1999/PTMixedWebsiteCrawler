import scrapy
class TaiwaneseamericanHumansSpider(scrapy.Spider):
    name = 'taiwaneseamericanHumansSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/perspectives/', 'http://www.taiwaneseamerican.org/category/interviews/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('h2 *::text')[0].get(),
                'Blurb': post.css('.entry-content *::text')[0].get(),
                'Image': post.css('.text-center img::attr(src)').extract(),
                'Link': post.css('.read-more-link a::attr(href)').extract(),
                'OP': "Taiwanese American.org"
            }
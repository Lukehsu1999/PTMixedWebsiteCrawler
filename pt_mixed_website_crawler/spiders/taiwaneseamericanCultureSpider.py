import scrapy
class TaiwaneseamericanCultureSpider(scrapy.Spider):
    name = 'taiwaneseamericanCultureSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/arts-and-culture/','http://www.taiwaneseamerican.org/category/food-travel/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('h2 *::text')[0].get(),
                'Blurb': post.css('.entry-content *::text')[0].get(),
                'Image': post.css('.text-center img::attr(src)').extract()[0],
                'Link': post.css('.read-more-link a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
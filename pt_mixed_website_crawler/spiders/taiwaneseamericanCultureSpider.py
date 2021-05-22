import scrapy
class TaiwaneseamericanCultureSpider(scrapy.Spider):
    name = 'taiwaneseamericanCultureSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/arts-and-culture/','http://www.taiwaneseamerican.org/category/food-travel/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('h2 *::text')[0].get(),
                'content': post.css('.entry-content *::text')[0].get(),
                'image': post.css('.text-center img::attr(src)').extract(),
                'url': post.css('.read-more-link a::attr(href)').extract(),
                'source': "Taiwanese American.org"
            }
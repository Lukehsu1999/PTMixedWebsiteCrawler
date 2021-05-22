import scrapy
class TaiwaneseamericanPoliticsSpider(scrapy.Spider):
    name = 'taiwaneseamericanPoliticsSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/social-issues-and-politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('h2 *::text')[0].get(),
                'Blurb': post.css('.entry-content *::text')[0].get(),
                'Image': post.css('.text-center img::attr(src)').extract()[0],
                'Link': post.css('.read-more-link a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
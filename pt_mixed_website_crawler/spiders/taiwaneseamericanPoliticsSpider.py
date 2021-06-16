import scrapy
class TaiwaneseamericanPoliticsSpider(scrapy.Spider):
    name = 'taiwaneseamericanPoliticsSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/social-issues-and-politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('h2 *::text')[0].get(),
                'Blurb': post.css('.entry-content *::text')[0].get(),
                'Image': "https://static.wixstatic.com/media/3221e1_6f6d781619524c42b54b0b3a746f80fe~mv2.jpeg",
                'Link': post.css('.read-more-link a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
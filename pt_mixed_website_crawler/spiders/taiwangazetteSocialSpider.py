import scrapy
class TaiwangazetteSocialSpider(scrapy.Spider):
    name = 'taiwangazetteSocialSpider'
    start_urls = ['https://www.taiwangazette.org/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title--list a::text')[1].get(),
                'Blurb': post.css('.entry-excerpt em::text')[0].get(),
                'Image': post.css('.excerpt-thumb img::attr(data-src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
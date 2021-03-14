import scrapy
class TaiwangazetteSocialSpider(scrapy.Spider):
    name = 'taiwangazetteSocialSpider'
    start_urls = ['https://www.taiwangazette.org/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.entry-title--list a::text')[1].get(),
                'content': post.css('.entry-excerpt em::text')[0].get(),
                'image': post.css('.excerpt-thumb img::attr(data-src)').extract(),
                'url': post.css('.entry-title a::attr(href)').extract(),
            }
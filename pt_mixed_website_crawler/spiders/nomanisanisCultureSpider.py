import scrapy
class NewbloommagSocialSpider(scrapy.Spider):
    name = 'newbloommagSocialSpider'
    start_urls = ['https://nomanisanis.land/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.title a::text')[0].get(),
                'content': post.css('.excerpt ::text')[0].get(),
                'image': post.css('.mask img::attr(src)').extract(),
                'url': post.css('.read-more-wrap a::attr(href)').extract(),
            }
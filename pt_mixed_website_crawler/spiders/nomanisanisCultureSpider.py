import scrapy
class NewbloommagSocialSpider(scrapy.Spider):
    name = 'newbloommagSocialSpider'
    start_urls = ['https://nomanisanis.land/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.title a::text')[0].get(),
                'Blurb': post.css('.excerpt ::text')[0].get(),
                'Image': post.css('.mask img::attr(src)').extract(),
                'Link': post.css('.read-more-wrap a::attr(href)').extract(),
                'OP': "No Man Is An Island"
            }
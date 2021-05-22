import scrapy
class LausanSocialSpider(scrapy.Spider):
    name = 'lausanSocialSpider'
    start_urls = ['https://lausan.hk/category/deep-dive/', 'https://lausan.hk/category/quick-read/', 'https://lausan.hk/category/interview/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.title a::text')[0].get(),
                'Blurb': post.css('.excerpt ::text')[0].get(),
                'Image': post.css('.mask img::attr(src)').extract()[0],
                'Link': post.css('.title a::attr(href)').extract()[0],
                'OP': "Lausan"
            }
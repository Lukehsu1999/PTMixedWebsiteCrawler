import scrapy
class NewbloommagSocialSpider(scrapy.Spider):
    name = 'newbloommagSocialSpider'
    start_urls = ['https://newbloommag.net/category/main/social-movements/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.cb-post-title a::text')[0].get(),
                'Blurb': post.css('.cb-excerpt ::text')[0].get(),
                'Image': post.css('.cb-mask img::attr(src)').extract()[0],
                'Link': post.css('.cb-mask a::attr(href)').extract()[0],
                'OP': "New Bloom Mag"
            }
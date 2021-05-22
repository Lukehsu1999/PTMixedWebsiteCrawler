import scrapy
class NewbloommagCultureSpider(scrapy.Spider):
    name = 'newbloommagCultureSpider'
    start_urls = ['https://newbloommag.net/category/main/arts-and-culture/ ']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.cb-post-title a::text')[0].get(),
                'Blurb': post.css('.cb-excerpt ::text')[0].get(),
                'Image': post.css('.cb-mask img::attr(src)').extract()[0],
                'Link': post.css('.cb-mask a::attr(href)').extract()[0],
                'OP': "New Bloom"
            }
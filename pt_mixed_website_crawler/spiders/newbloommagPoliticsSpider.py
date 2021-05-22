import scrapy
class NewbloommagPoliticsSpider(scrapy.Spider):
    name = 'newbloommagPoliticsSpider'
    start_urls = ['https://newbloommag.net/category/main/politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.cb-post-title a::text')[0].get(),
                'Blurb': post.css('.cb-excerpt ::text')[0].get(),
                'Image': post.css('.cb-mask img::attr(src)').extract()[0],
                'Link': post.css('.cb-mask a::attr(href)').extract()[0],
                'OP': "New Bloom"
            }
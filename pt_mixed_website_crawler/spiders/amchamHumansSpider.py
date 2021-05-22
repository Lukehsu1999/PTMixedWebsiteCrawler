import scrapy
class AmchamHumansSpider(scrapy.Spider):
    name = 'amchamHumansSpider'
    start_urls = ['https://topics.amcham.com.tw/category/executive-suite/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('.entry-summary p::text')[0].get(),
                'Image': post.css('img::attr(src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "AmCham"
            }
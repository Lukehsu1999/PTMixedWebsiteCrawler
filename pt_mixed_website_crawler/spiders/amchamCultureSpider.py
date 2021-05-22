import scrapy
class AmchamCultureSpider(scrapy.Spider):
    name = 'amchamCultureSpider'
    start_urls = ['https://topics.amcham.com.tw/category/wine-dine/', 'https://topics.amcham.com.tw/category/travel-and-culture/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('.entry-summary p::text')[0].get(),
                'Image': post.css('img::attr(src)').extract(),
                'Link': post.css('.entry-title a::attr(href)').extract(),
                'OP': "AmCham"
            }
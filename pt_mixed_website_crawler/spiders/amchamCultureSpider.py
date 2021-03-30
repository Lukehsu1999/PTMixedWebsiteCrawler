import scrapy
class AmchamCultureSpider(scrapy.Spider):
    name = 'amchamCultureSpider'
    start_urls = ['https://topics.amcham.com.tw/category/wine-dine/', 'https://topics.amcham.com.tw/category/travel-and-culture/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.entry-title a::text')[0].get(),
                'content': post.css('.entry-summary p::text')[0].get(),
                'image': post.css('img::attr(src)').extract(),
                'url': post.css('.entry-title a::attr(href)').extract(),
            }
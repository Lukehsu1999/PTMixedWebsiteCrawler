import scrapy
class LausanPoliticsSpider(scrapy.Spider):
    name = 'lausanPoliticsSpider'
    start_urls = ['https://lausan.hk/category/blog/statement/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.title a::text')[0].get(),
                'content': post.css('.excerpt ::text')[0].get(),
                'image': post.css('.mask img::attr(src)').extract(),
                'url': post.css('.title a::attr(href)').extract(),
            }
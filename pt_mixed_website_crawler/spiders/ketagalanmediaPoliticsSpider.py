import scrapy
class KetagalanmediaPoliticsSpider(scrapy.Spider):
    name = 'ketagalanmediaPoliticsSpider'
    start_urls = ['https://ketagalanmedia.com/category/ps/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.entry-title a::text')[0].get(),
                'content': post.css('p::text')[3].get(),
                'image': post.css('img::attr(src)').extract(),
                'url': post.css('.entry-title a::attr(href)').extract(),
            }
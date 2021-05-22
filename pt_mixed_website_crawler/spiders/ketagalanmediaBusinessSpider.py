import scrapy
class KetagalanmediaBusinessSpider(scrapy.Spider):
    name = 'ketagalanmediaBusinessSpider'
    start_urls = ['https://ketagalanmedia.com/category/cl/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('p::text')[3].get(),
                'Image': post.css('img::attr(src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Ketagalan Media"
            }
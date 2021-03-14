import scrapy
class NewsSpider(scrapy.Spider):
    name = 'newspider'
    start_urls = ['https://newbloommag.net/category/main/politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.cb-post-title a::text')[0].get(),
                'content': post.css('.cb-excerpt ::text')[0].get()
            }
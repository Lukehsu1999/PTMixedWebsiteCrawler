import scrapy
class KetagalanmediaPoliticsSpider(scrapy.Spider):
    name = 'ketagalanmediaPoliticsSpider'
    start_urls = ['https://ketagalanmedia.com/category/ps/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Title': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('p::text')[3].get(),
                'Image': post.css('img::attr(src)').extract(),
                'Link': post.css('.entry-title a::attr(href)').extract(),
                'OP': "Ketagalan Media"
            }
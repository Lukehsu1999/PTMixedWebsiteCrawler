import scrapy
class TaiwaninsightPoliticsSpider(scrapy.Spider):
    name = 'taiwaninsightPoliticsSpider'
    start_urls = ['https://taiwaninsight.org/category/politics/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('.entry-content p::text')[0].get(),
                'Image': post.css('img::attr(src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
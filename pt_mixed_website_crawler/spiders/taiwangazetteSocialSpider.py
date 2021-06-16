import scrapy
class TaiwangazetteSocialSpider(scrapy.Spider):
    name = 'taiwangazetteSocialSpider'
    start_urls = ['https://www.taiwangazette.org/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title--list a::text')[1].get(),
                'Blurb': post.css('.entry-excerpt em::text')[0].get(),
                'Image': "https://static.wixstatic.com/media/3221e1_6f6d781619524c42b54b0b3a746f80fe~mv2.jpeg",
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
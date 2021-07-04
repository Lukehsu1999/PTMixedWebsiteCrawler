import scrapy
class TaiwangazetteSocialSpider(scrapy.Spider):
    name = 'taiwangazetteSocialSpider'
    start_urls = ['https://www.taiwangazette.org/']

    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title--list a::text')[1].get(),
                'Blurb': self.smart_truncate(post.css('.entry-excerpt em::text')[0].get()),
                'Image': post.css('.excerpt-thumb img::attr(data-src)').extract()[0],
                'Link': 'https://www.taiwangazette.org'+post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "The Taiwan Gazette"
            }
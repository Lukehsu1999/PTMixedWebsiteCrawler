import scrapy
class TaiwaneseamericanCultureSpider(scrapy.Spider):
    name = 'taiwaneseamericanCultureSpider'
    start_urls = ['http://www.taiwaneseamerican.org/category/arts-and-culture/','http://www.taiwaneseamerican.org/category/food-travel/']

    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('h2 *::text')[0].get(),
                'Blurb': self.smart_truncate(post.css('.entry-content *::text')[0].get()),
                'Image': "https://static.wixstatic.com/media/3221e1_6f6d781619524c42b54b0b3a746f80fe~mv2.jpeg",
                'Link': post.css('.read-more-link a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
import scrapy
class LausanPoliticsSpider(scrapy.Spider):
    name = 'lausanPoliticsSpider'
    start_urls = ['https://lausan.hk/category/blog/statement/']

    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.title a::text')[0].get(),
                'Blurb': self.smart_truncate(post.css('.excerpt ::text')[0].get()),
                'Image': post.css('.mask img::attr(src)').extract()[0],
                'Link': post.css('.title a::attr(href)').extract()[0],
                'OP': "Lausan"
            }
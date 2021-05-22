import scrapy
class TaiwantodayPoliticsSpider(scrapy.Spider):
    name = 'taiwantodayPoliticsSpider'
    start_urls = ['https://www.taiwantoday.tw/list_tt.php?unit=2&unitname=Politics-Top-News']

    def parse(self, response):
        for post in response.css('li'):
            yield {
                'Title': post.css('h3::text').get(),
                # 'Blurb': post.css('a::attr(href)').extract(),
                # 'Image': post.css('a::attr(href)').extract()[0],
                'Link': post.css('a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
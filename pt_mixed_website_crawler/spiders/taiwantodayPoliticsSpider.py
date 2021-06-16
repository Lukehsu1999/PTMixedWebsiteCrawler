import scrapy
class TaiwantodayPoliticsSpider(scrapy.Spider):
    name = 'taiwantodayPoliticsSpider'
    start_urls = ['https://www.taiwantoday.tw/list_tt.php?unit=2&unitname=Politics-Top-News']

    def parse(self, response):
        for post in response.css('li'):
            yield {
                'Topic': post.css('h3::text').get(),
                # 'Blurb': post.css('a::attr(href)').extract(),
                'Image': "https://static.wixstatic.com/media/3221e1_6f6d781619524c42b54b0b3a746f80fe~mv2.jpeg",
                'Link': post.css('a::attr(href)').extract()[0],
                'OP': "Taiwanese American.org"
            }
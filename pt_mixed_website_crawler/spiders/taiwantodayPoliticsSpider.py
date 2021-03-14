import scrapy
class TaiwantodayPoliticsSpider(scrapy.Spider):
    name = 'taiwantodayPoliticsSpider'
    start_urls = ['https://www.taiwantoday.tw/list_tt.php?unit=2&unitname=Politics-Top-News']

    def parse(self, response):
        for post in response.css('li'):
            yield {
                'title': post.css('h3::text').get(),
                # 'content': post.css('a::attr(href)').extract(),
                # 'image': post.css('a::attr(href)').extract(),
                'url': post.css('a::attr(href)').extract(),
            }
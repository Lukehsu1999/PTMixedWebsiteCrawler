import scrapy
class AmchamSocialSpider(scrapy.Spider):
    name = 'amchamSocialSpider'
    start_urls = ['https://topics.amcham.com.tw/category/editorial/', 'https://topics.amcham.com.tw/category/analysis/', 'https://topics.amcham.com.tw/category/issues/', 'https://topics.amcham.com.tw/category/cover-stories/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title a::text')[0].get(),
                'Blurb': post.css('.entry-summary p::text')[0].get(),
                'Image': post.css('img::attr(src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Taiwan Business Topics"
            }
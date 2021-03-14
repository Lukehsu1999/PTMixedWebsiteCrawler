import scrapy
class AmchamSocialSpider(scrapy.Spider):
    name = 'amchamSocialSpider'
    start_urls = ['https://topics.amcham.com.tw/category/editorial/', 'https://topics.amcham.com.tw/category/analysis/', 'https://topics.amcham.com.tw/category/issues/', 'https://topics.amcham.com.tw/category/cover-stories/']

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('.entry-title a::text')[0].get(),
                'content': post.css('.entry-summary p::text')[0].get(),
                'image': post.css('img::attr(src)').extract(),
                'url': post.css('.entry-title a::attr(href)').extract(),
            }
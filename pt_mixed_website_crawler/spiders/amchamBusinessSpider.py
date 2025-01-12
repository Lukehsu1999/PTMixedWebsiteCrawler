import scrapy
class AmchamBusinessSpider(scrapy.Spider):
    name = 'amchamBusinessSpider'
    start_urls = ['https://topics.amcham.com.tw/category/industry-focus/', 'https://topics.amcham.com.tw/category/taiwan-business/']

    # Custom settings to address potential blocks
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'ROBOTSTXT_OBEY': False,  # Disable obeying robots.txt
        'COOKIES_ENABLED': True,  # Enable cookies to maintain session
        'RETRY_ENABLED': True,    # Enable retries for failed requests
        'RETRY_TIMES': 5,         # Retry up to 5 times
        'DOWNLOAD_DELAY': 1.0,    # Add delay between requests to avoid being blocked
    }
    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.entry-title a::text')[0].get(),
                'Blurb': self.smart_truncate(post.css('.entry-summary p::text')[0].get()),
                'Image': post.css('img::attr(src)').extract()[0],
                'Link': post.css('.entry-title a::attr(href)').extract()[0],
                'OP': "Taiwan Business Topics"
            }
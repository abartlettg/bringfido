from bringfido.items import BringfidoItem
from scrapy import Spider, Request

class BringfidoSpider(Spider):
    name = 'bringfido_spider'
    allowed_urls = ['https://www.bringfido.com']
    start_urls = ['https://www.bringfido.com/restaurant/']

    def parse(self, response):
        
        # Method 1: Getting a subset of URLS to start
        url_list = [f'https://www.bringfido.com/restaurant/{i}'
        for i in range(52142,52148)]
        url_list

        for url in url_list[:3]:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
        # print('='*55)
        # print('Hooray!  We called the parse_result_page() method!')
        # print(f'{response.url}')
        # print('='*55)
        rname = response.xpath('//h1[@class="h h--top h--bottom"]').extract()

    def parse_product_page(self, response):
        pass


        
    
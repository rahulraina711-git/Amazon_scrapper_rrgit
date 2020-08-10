import scrapy
from ..items import AmzscrapItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    pg_no = 2
    start_urls = [
        'https://www.amazon.in/s?k=python+programming+books&i=stripbooks&crid=2RE8MH3S35LCT&sprefix=python%2Cstripbooks%2C394&ref=nb_sb_ss_organic-diversity_1_6'
    ]

    def parse(self, response):
        items = AmzscrapItem()

        item_name = response.css('.a-color-base.a-text-normal::text').extract()
        item_price = response.css('.a-price-whole::text').extract()
        item_rating = response.css('a-icon-alt::text').extract()
        item_image = response.css('.s-image::attr(src)').extract()

        items['item_name'] = item_name
        items['item_price'] = item_price
        items['item_rating'] = item_rating
        items['item_image'] = item_image

        yield items
        # creating pagination
        next_page = 'https://www.amazon.in/s?k=python+programming+books&i=stripbooks&page='+ str(AmazonSpiderSpider.pg_no) +'&crid=2RE8MH3S35LCT&qid=1597082119&sprefix=python%2Cstripbooks%2C394&ref=sr_pg_2'
        if AmazonSpiderSpider.pg_no <= 5:

            AmazonSpiderSpider.pg_no += 1

            yield  response.follow(next_page, callback= self.parse)


import scrapy
import time 

# creating a new class to implement spider
class ReviewsSpider(scrapy.Spider):
    name = 'spider'
    custom_settings = {'DOWNLOAD_DELAY': 2,}
    #domain names to scrape
    allowed_domains = ['trustpilot.com']
    myBaseUrl = 'https://www.trustpilot.com/review/zaful.com'
    start_urls=['https://www.trustpilot.com/review/zaful.com?page=1']

   #defining a scrapy parser
    def parse(self, response):
        for quote in response.css('article.review'):
            yield {'star': quote.css('div.star-rating img::attr(alt)').get(),
                   'title': quote.css('h2.review-content__title a::text').get(),
                   'review': quote.css('p.review-content__text::text').getall()}

        next_page = response.css(".next-page::attr(href)")

        if next_page is not None:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
     
       

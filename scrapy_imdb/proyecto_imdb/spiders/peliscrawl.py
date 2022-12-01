import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto_imdb.items import ImdbItem
from scrapy.exceptions import CloseSpider

class PelisCrawl(CrawlSpider):
    name = 'peliscrawl'
    allowed_domains = ['www.imdb.com']
    item_count = 0
    
    # start_urls = ['https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&ref_=adv_prv']
    start_urls = ['https://www.imdb.com/search/title/?title_type=movie&genres=comedy&explore=title_type,genres&ref_=adv_prv']
    

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('(//a[@class="lister-page-next next-page"])[1]'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h3[@class="lister-item-header"]')), callback = 'parse_item', follow=False),
        # Rule(LinkExtractor(allow=(), restrict_css=(".desc > a::attr(href)"))),
        


    )

    def parse_item(self, response):
        
        item = {}
        puesto = response.xpath("(//div[@class='sc-edc76a2-1 gopMqI']/text())[1]").get()
        titulo = response.css("h1.sc-b73cd867-0::text").get()
        userrev = response.css('.sc-3ff39621-0 li:nth-child(1) .score::text').get()
        critrev = response.css('.sc-3ff39621-0 li:nth-child(2) .score::text').get()
        director = response.xpath("//div[@class='sc-7643a8e3-4 iAthmE']/div[@role='presentation']/ul[@role='presentation']/li[1]/div[1]/ul[1]/li[1]/a[1]/text()").get()
        reparto = response.xpath("//a[contains(@class,'sc-bfec09a1-1 gfeYgX')]/text()").getall()

        print(self.item_count)
        print('Popularidad:', puesto, 'Título:', titulo)
        print('Reseñas de usuarios: ', userrev, 'Reseñas de críticos: ', critrev)
        print('Director: ', director)
        print('reparto: ',reparto)

        item['puesto'] = response.xpath("(//div[@class='sc-edc76a2-1 gopMqI']/text())[1]").get()
        item['titulo'] = response.css("h1.sc-b73cd867-0::text").get()
        item['userrev'] = response.css('.sc-3ff39621-0 li:nth-child(1) .score::text').get()
        item['critrev'] = response.css('.sc-3ff39621-0 li:nth-child(2) .score::text').get()
        item['director'] = response.xpath("//div[@class='sc-7643a8e3-4 iAthmE']/div[@role='presentation']/ul[@role='presentation']/li[1]/div[1]/ul[1]/li[1]/a[1]/text()").get()
        item['reparto'] = response.xpath("//a[contains(@class,'sc-bfec09a1-1 gfeYgX')]/text()").getall()

        print('otro titulo: ', item[titulo])
        self.item_count+=1
        if self.item_count > 70:
            raise CloseSpider('Limite de items superado')
        yield item



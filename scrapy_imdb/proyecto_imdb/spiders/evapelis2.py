import scrapy


class Evapelis2Spider(scrapy.Spider):
    name = 'evapelis2'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0472954/?ref_=adv_li_tt/']

    def parse(self, response):
        
        # movie = response.css('.sc-80d4314-2')
        
        puesto = response.xpath("(//div[@class='sc-edc76a2-1 gopMqI']/text())[1]").get()
        title = response.xpath("//h1[@class='sc-b73cd867-0 eKrKux']/text()").get()
        #title = response.css('.sc-b73cd867-0 eKrKux::text').get()
        userrev = response.css('.sc-3ff39621-0 li:nth-child(1) .score::text').get()
        critrev = response.css('.sc-3ff39621-0 li:nth-child(2) .score::text').get()
        direccion = response.css('.sc-bfec09a1-8 > li:nth-child(1) >  div > ul > li > a').get()
                
        print('esto es una linea de control')
        print('posicion', puesto, 'título:', title)
        print('criticas de usuario: ', userrev, 'criticas de críticos: ', critrev)


        
        
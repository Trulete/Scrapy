import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    initial_url = 'https://www.imdb.com'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        pass

        movies= response.css('tbody.lister-list > tr > td.titleColumn')
        # movies= response.css('.lister-list > tr > .titleColumn')
        print("RESULTADO: ",len(movies))
        for movie in movies:
            title = movie.css('a::text').get()
            href = movie.css('a::attr(href)').extract()
            link = self.initial_url + href[0]
            print('movie:', title)
            print('enlace',link)


# //*[@id="main"]/div/span/div/div/div[3]
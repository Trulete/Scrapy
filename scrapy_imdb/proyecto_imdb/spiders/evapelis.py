import scrapy


class EvapelisSpider(scrapy.Spider):
    name = 'evapelis'
    allowed_domains = ['www.imdb.com']
    pagina = 1 #esta variable ayudará de cara la paginación
    start_urls = ['https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&ref_=adv_prv']

    def parse(self, response):
        
        # Extracción de información
        movies= response.css('.lister-list > .lister-item')
        
        for movie in movies:
            puesto = movie.css('.lister-item-index::text').get()
            title = movie.css('.lister-item-header > a::text').get()
            
            print('posicion',puesto, 'título:', title)
        
        
        siguiente = response.css(".desc > a::attr(href)").extract() # Si hay enlace a next, se captura aquí
        num_pag = (EvapelisSpider.pagina * 50) + 1 # El numero de página y por qué pelicula debe empezar
        next_page ='https://www.imdb.com/search/title/?genres=comedy&start='+str(num_pag)+'&explore=title_type,genres&ref_=adv_nxt' # Se construye la cadena del enlace siguiente
        
        if EvapelisSpider.pagina < 15 and siguiente is not None: # Se fija el numero de paginas a extraer y el control que para en caso de existir menos páginas
            EvapelisSpider.pagina+=1 # Se suma al índíce de página para siguiente iteracion
            yield response.follow(next_page, callback=self.parse)
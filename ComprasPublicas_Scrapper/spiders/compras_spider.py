import scrapy 
from scrapy_splash import SplashRequest 

class MySpider(scrapy.Spider): 
    name = 'login'
    start_urls = ["http://example.com", "http://example.com/foo"] 
    
    def start_requests(self): 
        for url in self.start_urls: 
            yield SplashRequest(url, self.parse, 
                endpoint='render.html', 
                args={'wait': 0.5}, 
           ) 

    def parse(self, response): 
        # response.body is a result of render.html call; it 
        # contains HTML processed by a browser. 
        # …
        print("\nPRINTING RESPONSE")
        print(response.body)
        print("\n")

"""
def authentication_failed(response):
    print("\nPRINTING RESPONSE")
    print(response)
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginSpider(scrapy.Spider):
    name = 'login'

    def start_requests(self):
        #urls = ['http://www.example.com/users/login.php']
        urls = ['http://www.compraspublicas.gob.ec/ProcesoContratacion/compras/index.php']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        #print(f"\n{response}\n")
        #return response
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login)

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
"""

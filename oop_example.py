import requests

class url:
    # Class attribute
    attr = "Class attribute"

    # Magic method
    def __init__(self, uri):
        self.uri = uri

    # Instance method
    def status_code(self):
        r = requests.get(self.uri)
        print(r.status_code)
    
    # Instance method
    def response(self):
        r = requests.get(self.uri)
        print(r.text)

    # Instance method
    def header(self):
        r = requests.get(self.uri)
        print(r.headers)        

amazon = url("https://amazon.com")

amazon.status_code()
amazon.header()
amazon.response()

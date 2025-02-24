from torpy.http.requests import TorRequests  

def scrape_onion(url):  
    with TorRequests() as tor_session:  
        return tor_session.get(url).text  

import requests  

def clone_site(url):  
    response = requests.get(url)  
    with open("clone.html", "w") as f:  
        f.write(response.text)  
    print("[+] Site cloned. Host with: php -S 0.0.0.0:80")  

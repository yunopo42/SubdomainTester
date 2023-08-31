import requests
target_input = "google.com"

def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"{word} is didn't ")
        pass

with open("subdomainlist.txt" , "r") as subdomainlist:
    '''#print(subdomainlist.read()) veya
    x = subdomainlist.read()
    print(x)
    '''
    for word in subdomainlist:
        word = word.strip() # kelimelerin yanında olan boşlukları temizler.
        url = "http://" + word + "." + target_input
        response = make_requests(url)
        if response is not None:  #diyerek kontrol edebiliriz yada direk if response: yeterli
            print(f"Found Subdomain ---> {url}")
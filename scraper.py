from bs4 import BeautifulSoup
import requests

def check_keywords():
    url = 'https://www.palmettopanthers.org'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
 
    urls = []
    for link in soup.find_all('a'):
        if(link.get('href')[:8] == 'https://'):
            urls.append(link.get('href'))
            #print(link.get('href'))
    
    return urls
    

if __name__ == '__main__':
    print(check_keywords([]))
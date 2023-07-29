import requests
import urllib.parse
token = "bebb86d82b384b0b945afc5f6759962fd6cbe1c4750"
targetUrl = urllib.parse.quote("https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1=%28factor*+OR+featur*+OR+variabl*+OR+caus*+OR+character*%29+AND+%28affect*+OR+contribut*+OR+produc*+OR+generat*+OR+conduc*%29+AND+%28ghg+OR+greenhouse+gas*%29+AND+%28indonesia+OR+indonesian%29&sid=9b2e60e27bfe6b6bc8f32af6fa95a6ee&sot=b&sdt=b&sl=191&s=TITLE-ABS-KEY%28%28factor*+OR+featur*+OR+variabl*+OR+caus*+OR+character*%29+AND+%28affect*+OR+contribut*+OR+produc*+OR+generat*+OR+conduc*%29+AND+%28ghg+OR+greenhouse+gas*%29+AND+%28indonesia+OR+indonesian%29%29&origin=searchbasic&editSaveSearch=&yearFrom=Before+1960&yearTo=Present&sessionSearchId=9b2e60e27bfe6b6bc8f32af6fa95a6ee&limit=10")
url = "http://api.scrape.do?token={}&url={}".format(token, targetUrl)
response = requests.request("GET", url)
print(response.text)

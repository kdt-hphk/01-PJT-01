import requests
from pprint import pprint
BASE_URL = 'https://api.themoviedb.org./3/'
path = 'movie/top_rated'
params = {  
    'api_key': '6d370233a737309005e5afd1cd9a6600',
    'language' : 'ko-KR'}

response = requests.get(BASE_URL+path, params=params)
print(response.json())
def vote_average_movies():
    avr8 = []
    BASE_URL = 'https://api.themoviedb.org./3/'
    response = requests.get(BASE_URL)
    dic = response.json()

    detail = dic.get('results', None)
    for detail in dic:
        vavr = detail.get('vote_average', None)
        if vavr >= 8:
            avr8.append(detail)
    return avr8
if __name__ == '__main__':
    pprint(vote_average_movies())    
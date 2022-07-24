import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
    'language': 'ko-KR',
    'page': 1}

response = requests.get(BASE_URL+path, params=params)
data = response.json()
li = data.get('results')


def ranking():
    pass
    a = sorted(li, key=lambda x: x['vote_average'], reverse=True)
    result = a[:5]
    return result

if __name__ == '__main__':
    pprint(ranking())
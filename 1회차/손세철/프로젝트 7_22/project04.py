import requests
from pprint import pprint

def recommendation(title):
    pass

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    URL = BASE_URL + path
    params = {
        'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(
        URL, params=params).json().get('results')

    if len(response) == 0:
        return None

    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = '/movie/'+str(response[0].get('id'))+'/recommendations'
    URL2 = BASE_URL2 + path2
    params = {
        'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
        'language': 'ko-KR',
    }

    result = []
    response2 = requests.get(URL2, params=params).json().get('results')

    for i in response2:
        result.append(i.get('title'))

    return result

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))

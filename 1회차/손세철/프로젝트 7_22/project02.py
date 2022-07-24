import requests
from pprint import pprint
def vote_average_movies():
    pass 
    BASE_URL = 'https://api.themoviedb.org./3/'
    path = 'movie/popular'
    params = {  
    'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
    'language' : 'ko-KR'}

    response = requests.get(BASE_URL+path, params).json()
    results = response['results']
    good_movies =[]
    for i in results:
        if type(i) == dict:
            points = i.get('vote_average')
            if points >= 8:
                good_movies.append(i)

    return good_movies
if __name__ == '__main__':
        pprint(vote_average_movies())
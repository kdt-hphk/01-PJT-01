import requests
from pprint import pprint


def credits(title):
    pass 

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
        'language': 'ko-KR',
        'query': title
    }

    res = requests.get(BASE_URL + path, params).json()

    if res['results']:
        movie_id = res['results'][0]['id']
        path2 = f'/movie/{movie_id}/credits'
        params2 = {
            'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
            'language': 'ko-KR',
            'query': movie_id
        }

        res2 = requests.get(BASE_URL + path2, params2).json()
        cast = []    
        for i in res2["cast"]:
            if i['cast_id'] < 10:
                cast.append(i['name'])
        crew = []    
        for j in res2["crew"]:
            if j['department'] == 'Directing' :
                crew.append(j['name'])

        person = {}
        person["cast"] = cast
        person["crew"] = crew

        return person
    else:
        return None
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
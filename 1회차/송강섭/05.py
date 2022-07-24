# - 영화 데이터 `movie.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - `id`, `title,` `vote_average`, `overview`, `genre_names`로 결과를 만듭니다. **(결과 예시 참고)**
#     - genre_names는 각 장르 정보를 값으로 가집니다.
#     - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

import json
from pprint import pprint


def movie_info(movie, genres):
    g_name = []
    for ids in movie['genre_ids']: # 무비의 제너럴아이디를 ids로 반복돌림
        for a in genres: # 이중반복문으로 제너럴을 a로 반복돌림
            if a['id'] == ids: # 그 a의 id가 18,80이랑 같으면?
                g_name.append(a.get('name')) # 리스트안에 +해줌 같은것의 이름을(값)
    movie['genre_ids'] = g_name
    result = {           # 값을 뽑아서 딕셔너리로 만들어서 넘기면 된다!
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_name' : movie.get('genre_ids')
    }
    return result
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
import json
from pprint import pprint


def movie_info(movie):
    result = {
    "genre_ids": movie.get("genre_ids"),
    "id": movie.get("id"),
    "title": movie.get('title'),
    "overview": movie.get("overview"),
    "title": movie.get("title"),
    "vote_average": movie.get("vote_average")
} 
    print(result)

    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
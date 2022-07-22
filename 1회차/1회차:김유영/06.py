import json
from pprint import pprint


def movie_info(movies, genres):
    pass
    result_m = []
    for movie in movies:
        genre_id = movie["genre_ids"]
        a = []
        for i in genre_id:
                for genre in genres:
                    if genre["id"] == i:
                        a.append(genre["name"])
                    
        result = {
        "genre_names": a,
        "id": movie.get("id"), 
        "title": movie.get("title"),
        "overview": movie.get("overview"),
        "title": movie.get("title"),
        "vote_average": movie.get("vote_average")
        }
        
        result_m.append(result)

        return result_m
    # 여기에 코드를 작성합니다.  
        
       
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
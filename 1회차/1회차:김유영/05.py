import json
from pprint import pprint

# genre_ide 안에 인덱스 18 일때
# 반복문이 돌 때 18과 id 가 같으면 
# value값을 넣은다.
def movie_info(movie, genres):
    pass
    name =[]
    for mv in movie["genre_ids"]:
        for genre in genres:
            if genre["id"] == mv:
                name.append(genre["name"])
                
    result = {
        "genre_name": name,
        "id": movie.get("id"),
        "title": movie.get('title'),
        "overview": movie.get("overview"),
        "title": movie.get("title"),
        "vote_average": movie.get("vote_average")
    }

    return result
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
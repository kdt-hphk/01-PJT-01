with open('04.txt', 'w', encoding = 'utf-8') as f:
    import json
from pprint import pprint

def movie_info(movie):
    return {'genre_ids' : movie['genre_ids'],
            'id' : movie['id'],
            'overview' : movie['overview'],
            'title' : movie['title'],
            'vote_average' : movie['vote_average']}

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))
    a = movie_info(movie)
for i in a['genre_ids'] :
    print(i+6) 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))

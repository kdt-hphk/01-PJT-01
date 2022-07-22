import json
from pprint import pprint

movie_info_idx = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
movie_info_dict = {}

def movie_info(movie):
    
    for i in range(len(movie_info_idx)):
        for j in movie:
            if movie_info_idx[i] == j:
                movie_info_dict[movie_info_idx[i]] = movie.get(j)

    return movie_info_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
import json
from pprint import pprint

movie_info_idx = ['id', 'title', 'vote_average', 'overview']
movie_info_dict = {}

def movie_info(movie, genres):

    for i in range(len(movie_info_idx)):
        for j in movie:
            if movie_info_idx[i] == j:
                movie_info_dict[movie_info_idx[i]] = movie.get(j)

    temp_dict = {}
    temp_list = []

    for a in range(len(genres_list)):
        temp_dict = genres_list[a] 

        if temp_dict['id'] in movie['genre_ids']: 
            temp_list.append(temp_dict["name"])

            movie_info_dict["genres_name"] = temp_list 
            
    return movie_info_dict
        

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
import json
from pprint import pprint
from sre_constants import RANGE

movie_info_idx = ['id', 'title', 'vote_average', 'overview']
movie_info_dict = {} 
movie_info_dict_final = []  

def movie_info(movies_list, genres_list): 

    temp_movie_info_dict = {}

    for i_2 in range(len(movies_list)): 
        temp_movie_info_dict = movies_list[i_2] #

        for i in range(len(movie_info_idx)):
            for j in temp_movie_info_dict:
                if movie_info_idx[i] == j:
                    movie_info_dict[movie_info_idx[i]] = temp_movie_info_dict.get(j) 

    
        temp_dict = {}
        temp_list = []

        for a in range(len(genres_list)):
            temp_dict = genres_list[a] 
       
            if temp_dict['id'] in temp_movie_info_dict['genre_ids']: 
                temp_list.append(temp_dict["name"]) 
                movie_info_dict["genres_name"] = temp_list 
            

        movie_info_dict_final.append(movie_info_dict) 
        
    
    return movie_info_dict_final
         

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
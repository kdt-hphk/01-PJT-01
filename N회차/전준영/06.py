import json
from pprint import pprint


def movie_info(movies, genres):
    dictionary0=[]
    dict0={}
    for movie in movies:
        dictionary0.append({})
        dict0=dictionary0[len(dictionary0)-1]
        dict0['genre_names']=[]
        cnt=0
        for i in genres:
            if(i["id"]== movie['genre_ids'][cnt]):
                dict0['genre_names'].append(i["name"])
        dict0['id']=movie['id']
        dict0['overview']=movie['overview']
        dict0['title']=movie['title']
        dict0['vote_average']=movie['vote_average']
    return dictionary0
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open(r'C:\Users\young\OneDrive\바탕 화면\01-PJT-01\N회차\전준영\data\movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open(r'C:\Users\young\OneDrive\바탕 화면\01-PJT-01\N회차\전준영\data\genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
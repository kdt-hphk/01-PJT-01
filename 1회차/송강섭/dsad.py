import json
from pprint import pprint
# movies는 movie가 여러개 있음, 각 movie마다 딕셔너리 형태
# 한 개의 딕셔너리 안에 5번에서 간추렸던 정보들을 모두 넣고 하나의 리스트 안에 차례대로 넣어야함
# 전체 리스트인 mvs_list를 만들고 각 mvs_list안에 result란 딕셔너리를 각각 한 번씩 넣음
# 그리고 result 딕셔너리 안의 genre_ids를 가져오기 위해 genres JSON파일에서 정보를 가져와서 5번과 마찬가지로 수행
#@ 처음에는 mvs_list안에 딕셔너리만 있는게 아니라 딕셔너리를 감싸는 리스트가 추가적으로 들어가있었음
#@ 이런식으로 문제별 / 상황별 적절한 자료구조 형태를 출력 해내는 능력이 정말 중요!!
def movie_info(movies, genres):
    mvs_list = []
    for movie in movies:
        mv_list = []
        for i in genres:
            for j in movie.get('genre_ids'):
                if j == i.get('id') :
                    mv_list.append(i.get('name'))
        result = {
        'genre_names': mv_list,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        }
        mvs_list.append(result)
    return mvs_list
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
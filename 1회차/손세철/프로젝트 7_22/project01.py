import requests
BASE_URL = 'https://api.themoviedb.org./3/'
path = 'movie/popular'
params = {  
    'api_key': 'fcf32c56bae1b94a4712878e7688ec3d',
    'language' : 'ko-KR'}

response = requests.get(BASE_URL+path, params=params)
print(response.json())

def popular_count():
    BASE_URL = 'https://api.themoviedb.org./3/'  
response = requests.get(BASE_URL+path, params=params).json()
count = 0
for i in response.get('results'):
    count += 1
print(count)
if __name__=='__title__':
    print(popular_count())
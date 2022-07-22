# 과일의 이름과 등장횟수
# 불러와서 개행으로 split들을 나눔


with open ('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/fruits.txt','r',encoding = 'utf-8') as c:
    p = c.read()
    fruits = p.split('\n')
    dict = {}
    for fruit in fruits:
        if fruit not in dict:
            dict[fruit] = 1
        else:
            dict[fruit] += 1

with open ('03.txt','w',encoding= 'utf-8') as c:
    for k, v in dict.items():
        c.write(f'{k} {v}\n')
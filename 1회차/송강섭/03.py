# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.
from pprint import pprint

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    
    names = dict()
    for i in f:
        i = i.strip()
        names[i] = names.get(i, 0) + 1
    pprint(names)

with open('03.txt','w', encoding='utf-8') as f2:
    for k, v in names.items():
        f2.write(f"{k} {v}\n")
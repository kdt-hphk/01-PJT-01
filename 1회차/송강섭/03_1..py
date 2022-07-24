import pprint


with open('data/fruits.txt','r', encoding='utf-8') as f:
    
    dic = dict()
    for i in f:
        i = i.strip()
        dic[i] = dic.get(i, 0) + 1
    pprint.pprint(dic)

with open('03.txt','w', encoding='utf-8') as f2:
    for k, v in dic.items():
        f2.write(f"{k} {v}\n") 
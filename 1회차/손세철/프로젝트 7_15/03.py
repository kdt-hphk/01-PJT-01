# 03. 텍스트 데이터 활용 - 등장 횟수
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    result = {}
    fruit_list = str.split('\n')
    for fruit in fruit_list:
        findcheck = fruit in result
        if (findcheck == False):
            result[fruit] = 1
        else:
            result[fruit] += 1
with open('03.txt', 'w', encoding='utf-8') as f:
    for i in result:
        f.write(f'{i} {result[i]}\n') 
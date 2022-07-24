with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    text = f.read()
    name = text.split('\n')
    name1 = set(name)
    cnt = 0

    for i in name1 :
        if i.endswith('berry'): # i 마지막 문자에 'berry'를 포함하면
            cnt += 1
            result = name1     
with open('02.txt', 'w', encoding = 'utf-8') as f:
    f.write(f'{cnt}\n')

    for i in name1:
        if i.endswith('berry'): 
            f.write(f'{i}\n')
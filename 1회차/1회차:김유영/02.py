with open ('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/fruits.txt','r',encoding = 'utf-8') as b:
    p = b.read()
    fruits = p.split('\n')
    # 숫자는 겹치는 것이 있으면 cntdㅔ 추가
    # 만약 berry로 끝난다 
    cnt = 0
    chart = []
    for fruit in set(fruits):
        if fruit.endswith('berry'):
            cnt += 1
            chart.append(fruit)

with open ('02.txt','w', encoding = 'utf-8') as b:
    b.write(f'{cnt}\n')
    for u in chart:
        b.write(f'{u}\n')

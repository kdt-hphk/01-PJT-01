with open('/Users/yuyeong/Desktop/프로젝트/01-PJT-01/N회차/홍길동/data/fruits.txt','r',encoding = 'utf-8')as a:
    cnt = 0
    for i in a:
        if True:
            cnt += 1
    b = str(cnt)

with open ('01.txt','w',encoding = 'utf-8')as a:
    a.write(b)

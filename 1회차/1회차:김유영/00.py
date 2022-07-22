# 파일을 만들어서 작성 00.txt

with open('00.txt', 'w', encoding = 'utf-8') as f:
    f.write('N회차 홍길동\n')
    f.write('Hello, welcome Python!\n')
    for i in range(1,6):
        f.write(''f'{i}알차 파이썬 열심히 공부 중\n')
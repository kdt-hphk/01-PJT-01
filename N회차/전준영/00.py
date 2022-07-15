

str0='''2회차 전준영
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중'''
with open("00.txt",'w',encoding='utf-8') as file1:
    file1.write(str0)
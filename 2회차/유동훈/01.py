fruits_list = []

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits_list = f.read().split(sep='\n')
    
with open('01.txt', 'w', encoding= 'utf-8') as f:
    f.write(str(len(fruits_list)))
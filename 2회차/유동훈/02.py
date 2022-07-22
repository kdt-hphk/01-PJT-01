berry_list = []

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits_list = f.read().split(sep='\n')
    for name in set(fruits_list):
        if name.endswith('berry'):
            berry_list.append(name)

with open('02.txt', 'w', encoding= 'utf-8') as f:
    f.write(f'{str(len(berry_list))}\n')
    for name in set(berry_list):
            f.write(f'{name}\n')
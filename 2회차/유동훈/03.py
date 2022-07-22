fruits_number = {}

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits_list = f.read().split(sep='\n')
    for name in fruits_list:
        if not name in fruits_number:
            fruits_number[name] = 1
        else:
            fruits_number[name] += 1

with open('03.txt', 'w', encoding= 'utf-8') as f:
    for key in fruits_number:
        f.write(f'{key} {fruits_number[key]}\n')

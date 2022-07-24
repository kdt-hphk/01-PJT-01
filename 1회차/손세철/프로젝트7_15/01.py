with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    result = len(names)

with open('01.txt', 'w', encoding='utf-8') as ff:
    ff.write(str(result))
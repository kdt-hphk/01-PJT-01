with open(r"C:\Users\young\OneDrive\바탕 화면\01-PJT-01\N회차\전준영\data\fruits.txt","r",encoding="utf-8") as file0:
    str0=file0.read()
ls0=str0.split('\n')
with open('01.txt','w',encoding='utf-8') as file1:
    file1.write(str(len(ls0)))



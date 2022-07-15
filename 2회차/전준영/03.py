with open(r"C:\Users\young\OneDrive\바탕 화면\01-PJT-01\N회차\전준영\data\fruits.txt","r",encoding="utf-8") as file0:
    str0=file0.read()
ls0=str0.split('\n')
dict0={}
with open("03.txt",'w',encoding='utf=8') as file0:
    cnt=0
    for fr in ls0:
        if(fr in dict0):
            dict0[fr]+=1
        else:
            dict0[fr]=1
    for input in dict0:
        file0.write(str(input)+' '+str(dict0[input])+'\n')

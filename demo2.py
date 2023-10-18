f = open('bill.txt','r',encoding='UTF-8')
f_bak = open('bill.txt.bak','w',encoding='UTF-8')

for line in f:
    if line.count('测试')==0:
        f_bak.write(line)

f.close()
f_bak.close()
T = int(input())
if T<1 or T>(3*10**4):
    exit(0)
while (T != 0):
    s = input()
    n = len(s)
    if n<1 or n>50:
        exit(0)
    r = []
    flag = 1
    for i in range(n+18):
        r.append(0)
    for i in range(n):
        if s[i]=='.':
            continue
        num = int(s[i])
        if num >9 or num<0:
            exit(0)
        p = i+9
        for j in range (p-num,p+num+1):
            if r[j] == 1:
                flag = 0
                break
            r[j] = 1
        if flag == 0:
            break
    if flag == 0:
        print("unsafe")
    else:
        print("safe")
    T -= 1
'''
    c=[]
    for i in range(len(n)):
    if n[i]!='.':
        sub=1
        add=1
    for j in range(int(n[i])):
        c.append(int(n[i])-sub)
        c.append(int(n[i])+add)
        sub+=1
        add+=1
    k=0
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i]==c[j]:
                k=1
    if(k==1):
        print("unsafe")
    else:
        print("safe")
    T = T - 1

exit(0)'''
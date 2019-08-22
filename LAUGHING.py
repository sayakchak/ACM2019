def notarj(lis):
    temp = 0
    for i in range (len(lis)-1):
        if lis[i]>lis[i+1]:
            temp = 1
            break
    return temp
def not_same_intensity(lis): #constraint
    temp = 1
    l = []
    for x in lis:
        l.append(x)
    l.sort()
    for i in range(len(l)-1):
            if l[i] == l[i+1]:
                temp = 0
                break
    return temp
T = int(input())
if T<1 or T>100000: #constraint
    exit(0)
sum = 0
for i in range(T):
    N = int(input())
    sum += N #constraint
    if N<1 or N>100000: #constraint
        exit(0)
    if sum>1000000: #constraint
        exit(0)
    J = [int(x) for x in input().split()]
    for x in J:
        if (x!=1 and x!=-1): #constraint
            exit(0)
    L = [int(x) for x in input().split()]
    for x in L:
        if x<0 or x>1000000000:
            exit(0)
    if not_same_intensity(L) != 1: #constraint
        exit(0)
    err = 0
    if 1 in J:
        laugh = []
        l2 = []
        for i in range(len(J)):
            if J[i]==1:
                laugh.append(L[i])
                l2.append(L[i])
        if len(laugh)>1:
            for j in range(len(laugh)-1):
                if laugh[j] > laugh[j+1]:
                    err = 1
                    del laugh[j]
                    del l2[j+1]
                    if notarj(laugh) == 1 and notarj(l2) == 1:
                        err = 2
                    break
            
    if err>1:
        print("#itsnot_arjun")
    else:
        print("#laughing_arjun")
                        
                    

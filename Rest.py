T = int(input())
sum_n = 0
sum_m = 0
if T<1 or T>100:
    exit(0)
for i in range(T):
    N,M = [int(x) for x in input().split()]
    sum_n += N
    sum_m += M
    if sum_n>300000 or sum_m>100000 or N<1 or M<1 or N>100000 or M>100000:
        exit(0)
    L = []
    R =[]
    P = []
    val = []
    for j in range(N):
        l,r = [int(x) for x in input().split()]
        if l<1 or r<1 or l>=r or r>1000000000 or l>1000000000:
            exit(0)
        L.append(l)
        R.append(r)
    for j in range(M):
        p = int(input())
        if p<1 or p>1000000000:
            exit(0)
        P.append(p)
    L.sort()
    R.sort()
    #PAIRWISE DISJOINT OPTIMIZATION NOT DONE
    for j in range (len(P)):
        if L[0]>=P[j]:
            val.append(L[0] - P[j])
        elif R[-1]<=P[j]:
            val.append(-1)
        elif L[-1]<=P[j] and R[-1]> P[j]:
            val.append(0)
        else:
            for k in range(len(L)-1):
                if R[k]>P[j] and L[k] <= P[j]:
                    val.append(0)
                elif R[k]<=P[j] and L[k+1] >= P[j]:
                    val.append(L[k+1] - P[j])
    for j in range(1,len(val)):
        print(val[j])            
        
                
            


            

        
    
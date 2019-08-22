T = int(input())
def findxor(a,p):
    b = 0
    while(b>=0):
        if((a and not b) or (not a and b)) == p:
            return p
            break
        b+=1
for i in range(T):
    l,r = [int(x) for x in input().split()]
    A = [int (x) for x in input().split()]
    B = [int(x) for x in input().split()]
    P = 0
    for j in range (len(A)):
        if A[j] == B[j]:
            P += 1
    for j in range(Q):
        x, y, z = [int(x) for x in input().split()]
        l = findxor(x, P)
        y = findxor(y, P)
        z = findxor(z, P)
        P = 0
        for k  in range (l,r+1):
            if B[k] == c:
                P += 1
        print(P)
T = int(input())
if T<1 or T>5000:
    exit(0)
for t in range(T):
    n, k = [int(x) for x in input().split()]
    if 1>n or n>50 or k<1 or k>50000:
        exit(0)
    a = [int(x) for x in input().split()]
    a.sort()
    if a[0]<1  or a[-1]>50000:
        exit(0)
    S = 0
    #print(a)
    for i in range (n-1):
        if a[i]>k and a[i+1]>k:
            if (a[i]-k > k):
                #print(a[i])
                x = int((a[i]-k)/k) 
                y = (a[i]-k)%k
                sub = k*x + y
                #print(x)
                a[i] -= sub
                a[i+1] -= sub
            else:
                x = a[i] - k
                a[i] = k
                a[i+1] -= x
            #print(a)
        '''
        if i == n-2:
            while a[i]>k and a[i+1]>k:
                a[i] -= 1
                a[i+1] -= 1
                '''
        S += a[i]
    #print(a)
    print(S+a[-1])
    '''    
    l = -1
    for i in range (n):
        if a[i]>k:
            l = i
            break
    
    if l == (n-1):
        print(sum(a))
    else:
        S = sum(a[:l])
        n_largest = 1
        m  = a[-1]
        m2 = a[-1]
        for i in range(n-1,-1,-1):
            if a[i]<m:
                m2 = a[i]
                break
            n_largest+=1
        if (N-l)%2 == 0:
            if n_largest%2 == 0:
                S += ((N-l)*k)
            else:
                S += ((N-l-1)*k) + (m-k)
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
T = int(input())
if T<1 or T>100:
    exit(0)
for i in range (T):
    N = int(input())
    if N<1 or N>100:
        exit(0)
    count = 0
    for j in range(N):
        s,j = [int(x) for x in input().split()]
        if s<1 or j <1 or s>300 or j>300:
            exit(0)
        if (j-s) > 5:
            count += 1
    print(count)

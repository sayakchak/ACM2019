'''T = int(input())
if T<1 or T>1000:
    exit(0)
else:
    for i in range(T):
        count = 0
        c = [int(x) for x in input().split()]
        for x in c:
            if x == 1:
                count += 1
            else:
                count = 0
            if count == 6:
                break
        if count == 6:
            print("#coderlifematters")
        else:
            print("#allcodersarefun")'''

T = int(input())
if T<1 or T>1000:
    exit(0)
else:
    for i in range(T):
        c = input()
        d = "1 1 1 1 1 1"
        if d in c:
            print("#coderlifematters")
        else:
            print("#allcodersarefun")
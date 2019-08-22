T = int(input())
if T>100:
    exit(0)
for i in range(T):
    S = input()
    if len(S)>1000 or len(S)<1:
        exit(0)
    st = ""
    for c in S:
        add = ord(c)%26
        if add+ord(c)>ord('z'):
            st += chr(ord('a') + add - (ord('z') -ord(c))-1)
        else:
            st += chr(ord(c) + add) 
    print(st)
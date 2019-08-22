def compare(a,b,equal):
    dummy = "\0"
    for i in range(len(a),0,-1):
        if a[:i]==b[:i] and (a[:i] not in equal): 
            #print("equal",m)
            return a[:i]
    return dummy
def compare2(a,b,equal):
    dummy = "\0"
    for i in range(len(a)):
        if a[i:]==b[i:] and (a[i:] not in e): 
            #print("equal",m)
            return a[i:]
    return dummy
temp = ""
output = ""
y = 0
for test in range(int(input())):
    words = []
    equal = []
    w = []
    e = []
    y = 0
    for inp in range (int(input())):
        temp = input()
        w.append(temp)
        words.append(temp[::-1])
    #print(words)
    words.sort()
    #w.sort
    if len(words)>1:
        i = 0
        while i<(len(words)-1):
            tempo = compare(words[i],words[i+1],equal)
            if tempo != "\0" :
                equal.append(tempo)
                i+=2
            else: i += 1
        i = 0
        while i<(len(w)-1):
            tempo = compare2(w[i],w[i+1],e)
            if tempo != "\0" :
                e.append(tempo)
                i+=2
            else: i += 1
        y = max(len(equal)*2,len(e)*2)
    output += "Case #"+str(test+1)+": "+str(y)+"\n"
    print(equal,words,e,w)
print(output.rstrip('\n'))
s1 = 1
s2 = 2
t = s1 + s2
sum = 0
while (t < 4000000):
    s1 = s2
    s2 = t
    t = s1 + s2
    if t%2 == 0:
        sum += t
print (sum)


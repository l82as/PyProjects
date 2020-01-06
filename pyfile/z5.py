from math import ceil
n = int(input())
s = 0
a =[]
for i in range(n):
    a.append(int(input()))
a.append(0)
i = n-1
while True:
    
    c = 1
    s = a[n]
    for j in range(n-1, i-1, -1):
        
        
        s += a[j]
        c += 1

    for j in range(n-1, i-1, -1):
        a[j] = round(s/c)
    i -= 1
    a[n]=ceil(s/c)
    if max(a) == a[n]:
        break  
print(a[n])

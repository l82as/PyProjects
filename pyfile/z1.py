l = list( map(int, input().split()) )
log = False
for i in range(3):
    k = (i+2)%3
    n = (i+1)%3
    if l[i] == l[k] + l[n]:
        log = True
    
if log:
    print("Да")
else:
    print("Нет")


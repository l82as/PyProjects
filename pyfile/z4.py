def min_number1(n):
    if  n <= 9:
        return str(10+n-1)
    elif (n <= 18):
        return str((n-9)*10+9)
    else:
        return "not"
def min_number2(n):
    if n <= 9:
        return ('0' + str(n))
    elif (n <= 18):
        return str((n-9)*10+9)
    else:
        return "not"
a = input()
if len(a)% 2 == 0:
    x1 = int(a[:len(a)//2])
    x2 = int(a[len(a)//2:])
else:
    x1 = int(a[:len(a)//2+1])
    x2 = int(a[len(a)//2+1:])
num1 = min_number1(x1) + min_number2(x2)
num2 = min_number1(x2) + min_number2(x1)
if "not" in num1:
    num1 = 0
elif len(num1)!=4:
    num1 = 9999
else:
    num1 = int(num1)

if "not" in num2:
    num2 = 0
elif len(num2)!=4:
    num2 = 9999
else:
    num2 = int(num2)

print(min(num1, num2))

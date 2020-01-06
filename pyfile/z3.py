import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

S = (N//A)*B

S1 = ((N%A)//C) * D + (N%A)%C
if B < S1 and N%A!=0:
    S+=B
elif N%A == 0:
    f=0
else:
    S+=S1
M1 = S


A,C = C,A
B,D = D,B
    
S = (N//A)*B

S1 = ((N%A)//C) * D + (N%A)%C
if B < S1 and N%A!=0:
    S+=B
elif N%A == 0:
    f=0
else:
    S+=S1

M = S
print(min(M, M1))

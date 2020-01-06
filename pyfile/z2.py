N = int(input())
S = N//48
A = (N%48)//16
P = (N % 16)//4
V = N%4
print(S, A, P, V)


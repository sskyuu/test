a = "abcdefghijklmnopqrstuvwxyz"
def f(n):
    return int(n) - 1
P = list(map(f,input().split()))
l = []
for i in range(len(P)):
    l.append(a[P[i]])
print("".join(l))

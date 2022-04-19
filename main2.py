l = ["ABC","ARC","AGC","AHC"]
s = [input() for _ in range(3)]
x =set(s)
for i in l:
    if not i in x:
        print(i)
        exit()
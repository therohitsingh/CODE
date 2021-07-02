n = int(input("n:-"))
a = []
for i in range(0,n):
    a.append(int(input("a:-")))
a.sort()
print(a[-2])  
n = [1,2,2,1]
n1 = [2,2]

set1 = set(n)
print(set1)
set2 = set(n1)
print(set2)

for x in set1:
    if x in set2:
        print(set2)
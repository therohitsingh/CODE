from collections import defaultdict
data = defaultdict(list)

for _ in range(int(input())):
    name = input()
    score = float(input())
    data[score].append(name)
print(data)
key = sorted(data)[1]
print(key)
a = sorted(data[key])
print('\n'.join(a))
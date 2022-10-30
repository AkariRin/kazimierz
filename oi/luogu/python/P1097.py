c = int(input())
li = []
d = {}

while c > 0:
    li.append(int(input()))
    c -= 1

for i in li:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# 输出排序
li = list(d.keys())
li.sort()

for i in li:
    print(f'{i} {d[i]}')

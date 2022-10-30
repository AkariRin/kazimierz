n = int(input())
li = []
i = 1

while i**2 <= n:
    li.append(str(i**2))
    i += 1

print(' '.join(li))

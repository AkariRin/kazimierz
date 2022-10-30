n = int(input())
li = input().split()

for i in range(len(li) - 1, 0, -1):  # 比较次数
    for j in range(i):
        if int(li[j] + li[j + 1]) < int(li[j + 1] + li[j]):
            li[j], li[j + 1] = li[j + 1], li[j]

print(''.join(li))

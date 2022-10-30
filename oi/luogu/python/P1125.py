primelist = [11, 13, 17, 19, 2, 23, 29, 3, 31, 37, 41, 43, 47, 5, 53, 59, 61, 67, 7, 71, 73, 79, 83, 89, 97]
word = input()
d = {}

# 统计单词字母出现次数
for w in word:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

li = list(d.values())
li.sort()

n = li[-1] - li[0]
if n in primelist:
    print(f'Lucky Word\n{n}')
else:
    print('No Answer\n0')

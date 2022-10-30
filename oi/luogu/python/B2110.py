word = input()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
ind = len(word) - 1
output = 'no'

for i in letters:
    if word.count(i) == 1 and word.index(i) < ind:
        output = i
        ind = word.index(i)

print(output)

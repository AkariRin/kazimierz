c = int(input())
classmate = dict()
i = 0
while i < c:
    arg = input().split(' ')
    classmate[arg[1]] = int(arg[0])
    i += 1

max_score = 0
first = ''
for key, value in classmate.items():
    if value > max_score:
        max_score = value
        first = key

print(first)

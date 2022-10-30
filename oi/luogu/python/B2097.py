array_len = int(input())
li = input().split()
i = 1
x = 1
max_x = 0

while i < array_len:
    if li[i] == li[i - 1]:
        x += 1
    elif li[i] != li[i - 1] and max_x < x:
        max_x = x
        x = 1
    else:
        x = 1
    i += 1

print(max_x)

a = int(input())

if a > 0:
    a = int("".join(reversed(str(a))))
    print(a)
elif a < 0:
    a = abs(a)
    a = int("".join(reversed(str(a))))
    print('-' + str(a), sep='')
else:
    print(0)

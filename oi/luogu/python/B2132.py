i = 2
limit = int(input())
empty = True


# 判断是否为质数
def prime(n):
    param = 2
    while param * param <= n:
        if n % param == 0:
            return False
        param += 1
    return True


while i <= limit:
    if prime(i) and prime(i + 2) and i + 2 <= limit:
        empty = False
        print(i, i + 2)
    i += 1

if empty:
    print('empty')

n = int(input())
i = 0


# 斐波那契数列函数
def fib(m):
    if m == 0:
        return 0
    elif m == 1 or m == 2:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)


while i < n:
    x = int(input())
    print(fib(x))
    i += 1

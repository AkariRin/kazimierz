def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


i1 = 2
result = 0
inp = int(input())

while i1 < inp:
    if inp % i1 == 0:
        i2 = int(inp / i1)
        if prime(i1) and prime(i2) and i1 > i2:
            result = i1
        elif prime(i1) and prime(i2) and i1 < i2:
            result = i2
    i1 += 1

print(result)

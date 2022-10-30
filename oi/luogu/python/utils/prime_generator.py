import pyperclip
"""
打表脚本
生成从2到输入值的所有质数，以列表形式输出并自动复制到剪贴板
"""
x = int(input('>'))
li = []


def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


while x > 1:
    if prime(x):
        li.append(str(x))
    x -= 1

li.sort()

print(len(li))
output = ", ".join(li)
pyperclip.copy(f'[{output}]')

num = input() + "x"
# 以字符为键，以数量为值
key = ""
count = 0
res = ""

for i in range(len(num)):
    if key != num[i]:
        res = res + str(count)
        res = res + key
        count = 1
        key = num[i]
    else:
        count += 1

res = res.replace("0", "", 1)
print(res)

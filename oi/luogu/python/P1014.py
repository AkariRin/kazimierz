n = int(input())
up = False  # 这里确定线的方向朝上还是朝下
point = [1, 2]

if n == 1:  # 如果在(1,1)就直接输出
    print('1/1')
else:
    while n > 2:
        if not up and point[1] == 1:  # 方向向下并且碰到左侧边缘
            point[0] += 1
            up = True
        elif not up and point[1] != 1:  # 方向向下但未碰到左侧边缘
            point[0] += 1
            point[1] -= 1
        elif up and point[0] == 1:  # 方向向上并且碰到顶部边缘
            point[1] += 1
            up = False
        elif up and point[0] != 1:  # 方向向上但未碰到顶部边缘
            point[0] -= 1
            point[1] += 1
        n -= 1

    print(f'{point[0]}/{point[1]}')

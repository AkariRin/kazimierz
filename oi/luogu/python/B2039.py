ints = input().split()

if int(ints[0]) > int(ints[1]):
    print('>')
elif int(ints[0]) < int(ints[1]):
    print('<')
else:
    print('=')

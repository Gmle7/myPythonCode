help(hex)
i = int(input('请输入一个整数'))
print('十进制%s转为十六进制数为%s' % (i, hex(i)))
print(hex(65536))

def c_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(c_abs(111))

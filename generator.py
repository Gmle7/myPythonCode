#生成器
# G = (i * i for i in range(1, 11))
# for g in G:
#     print(g)

# def fibonacci(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield (b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# F = fibonacci(8)

# while True:
#     try:
#         x = next(F)
#         print('g', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

def pascalsTriangle():
    L=[1]
    while True:
        yield L
        L=[L[0]]+[L[n]+L[n+1] for n in range(len(L)-1)]+[L[-1]]

p=pascalsTriangle()
next(p)

# 生成器
g = (x * x for x in range(10))
print(type(g))

print(next(g))
print(next(g))
print(next(g))
for v in g:
    print(v)
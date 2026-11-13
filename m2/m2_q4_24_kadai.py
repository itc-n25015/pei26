
def func(x, y):
    return bool(x), bool(y), bool(x + y)

a = func(-5, -6)
z = list[a]

print(z)

# bool()関数は、値をTrueまたはFalse（真偽値）に変換する関数
# 0や空のリストはFalse、それ以外の数値や空でないリストはTrueになる

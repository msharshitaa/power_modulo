def power_modulo(a, b, c):
    if b == 0:
        return 1 % c
    res = power_modulo(a, b // 2, c)
    res = (res * res) % c
    if b % 2 == 0:
        return res
    else:
        return (res * a) % c
a = int(input())
b = int(input())
c = int(input())
print(power_modulo(a, b, c))

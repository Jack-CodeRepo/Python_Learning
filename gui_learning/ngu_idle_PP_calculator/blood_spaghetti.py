from math import log2

# 10**15 == 1 quadrillion
# 10**16 == 10 quadrillion
# 10**17 == 100 quadrillion
# 10**18 == 1 quintillion

blood = 10**16

calc = blood / 10000

result = log2(calc)


print(result)
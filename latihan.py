import math     #mengimpor modul math

# A
'''
def a(x):
    return x**2
'''
a = (lambda x: x**2)
a(5)

# B
'''
def b(x, y):
    return math.sqrt(x**2 + y**2)
'''
b = (lambda x,y: math.sqrt(x**2 + y**2))
b(4, 1)

# C
'''
def c(*args):
    return sum(args)/len(args)
'''
c = (lambda *args: sum(args)/len(args))
c(1, 3, 2)

# D
'''
def d(s):
    return "".join(set(s))
'''
d = (lambda s: "".join(set(s)))
d("Hello World")
d("Hello")

from math import tan, pi
from time import time

def vremya(func):
    def vremyafunc(*args):
        start = time()
        func(*args)
        print(f'Время, затраченное на выполнение функции: {time() - start}')
    return vremyafunc

def decorat(func):
    def name(*args):
        print(f'Была вызвана функция {func.__name__}')
        func(*args)
    return name


@vremya
@decorat
def s_mnogougolnika(n, s):
    print(n*s*s/(4*tan(pi/n)))

@vremya
@decorat
def summa_chisel(l):
    print(l*(l+1)/2)



n = int(input ("Введите количество сторон - "))
s = int(input ("Введите длину стороны - "))
s_mnogougolnika(n, s)

l = int(input("Введите значение l - "))
res = 0
for i in range(1, l + 1):
    res += i
summa_chisel(l)
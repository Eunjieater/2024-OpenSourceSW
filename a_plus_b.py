def week6(a, b, max):
    i = 0
    result = a*a*max+b
    while i <= max:
        week6(a, b, i)
        i = i + 1
    return (f'{a}x{a}x{max} + {b} = {result}')

a = int(input('a: '))
b = int(input('b: '))
max = int(input('Max: '))
week6(a, b, max)


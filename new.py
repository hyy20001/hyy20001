def hello_n(name: str,
            n: int):
    for i in range(n):
        print('Hello, ', name)


v = 'Vasya', 5
hello_n(*v)
i = 1
x = 1
while i == 1:
    x = input('Введите x ')
    x = int(x)
    x = x % 10
    print('остаток деления x на 10 = ', x)
    print('Продолжить? да=1')
    i = int(input())
cortege = 12, 14, 16, 18, 20, 21
a, b, *rest = cortege
c = len(cortege)
print('full length of cortege = ', c)
print(*cortege)
print(*rest, sep=':', end='\nThat is all folks!')

a = int(input('введи число: '))
n = 1
while True:
    s = 0
    for i in range(1, n + 1):
        s += 1 / i

    if s > a:
        print('1...', n - 1, sep='')
        break

    n += 1

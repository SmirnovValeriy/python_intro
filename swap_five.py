'''
num = 10^n * x_n + ... + 10^1 * x_1 + 10^0 * x_0
x_0 * num = x_0 * 10^n * x_n + ... + x_0 * 10^1 * x_1 + x_0 * 10^0 * x_0 (1)
x_0 * num = 10^n * x_0 + 10^(n-1) * x_n + ... + 10^0 * x_1               (2)
(1) - (2):
(10 * x_0 - 1) * (10^(n-1) * x_n + ... + 10^0 * x_1) = x_0 * (10^n - x_0)
(10^(n-1) * x_n + ... + 10^0 * x_1) = x_0 * (10^n - x_0) / (10 * x_0 - 1)
'''
k = int(input())
n = 0
while True:
    if (10 ** n - k) % (10 * k - 1) == 0:
        print((10 ** n - k) // (10 * k - 1) * k * 10 + k)
        break
    n += 1
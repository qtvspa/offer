# -*- coding:utf-8 -*-

""" 实现fibonacci数列"""


def fibonacci(num):

    a, b = 0, 1
    count = 0
    while count < num:
        a, b = b, a+b
        count += 1
        yield a


def fibonacci_dp(n):
    """ return f(n) """
    if not n:
        return 0

    dp = [0 for _ in range(n + 1)]

    if n >= 1:
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    if dp:
        return dp[n - 1] + dp[n - 2]


if __name__ == '__main__':

    # print([i for i in fibonacci(10)])
    print(fibonacci_dp(4))

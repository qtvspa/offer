
# 已知rand7()可以产生1~7的7个数(均匀概率),利用rand7() 产 生 rand10() 1~10(均匀概率)
# 思路：采用7进制


def rand7():
    import random
    return random.choice([1, 2, 3, 4, 5, 6, 7])


def rand10():
    i = rand7() - 1
    j = rand7() - 1

    # 7 * i + j 可以看作一个7进制的数，范围为00~66，转换为10进制就是0~48
    # 这些 7 进制数的产生概率都是一样的，每个数都是1/48，所以可以取0~39的这40个数，它们的概率也是相同的
    if (num := 7 * i + j) >= 40:
        return rand10()
    else:
        # 余10加1 即可
        return num % 10 + 1


if __name__ == '__main__':
    print(rand10())

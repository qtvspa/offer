
# 计算质数数量
# https://leetcode-cn.com/problems/count-primes/

# 暴力解法会超时
def count_primes(n: int) -> int:

    result = []

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

    return len(result)


# 埃氏筛（如果 x 是质数，那么大于 x 的 x 的倍数 2x,3x,… 一定不是质数）
def count_primes2(n: int) -> int:

    is_prime_dict = {num: True for num in range(1, n + 1)}
    count = 0

    for i in range(2, n):
        if is_prime_dict[i] is True:
            count += 1
            for j in range(2 * i, n, i):
                is_prime_dict[j] = False

    return count


if __name__ == '__main__':
    print(count_primes2(100))


# 单调递增的数字
# https://leetcode-cn.com/problems/monotone-increasing-digits/
# 思路：见注释


def monotone_increasing_digits(n: int) -> int:

    list_n = list(str(n))
    r = len(list_n) - 1
    res = []

    # 从右往左遍历
    while r - 1 >= 0:
        # 如果当前元素大于或等于前一个元素，则将当前元素加入res
        if list_n[r] >= list_n[r - 1]:
            res.append(list_n[r])
        # 否则把刚刚加入res的所有值全变成'9'，并将前一个元素减1
        else:
            list_n[r - 1] = str(int(list_n[r - 1]) - 1)
            res = ['9'] * (len(res) + 1)
        r -= 1

    # 考虑第一个元素是否为0，不为0，则加入res
    if list_n[r] != '0':
        res.append(list_n[r])

    # 返回res的逆序
    return int(''.join(res[::-1]))


if __name__ == '__main__':
    print(monotone_increasing_digits(963856657))

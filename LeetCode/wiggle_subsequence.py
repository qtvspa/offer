from typing import List

# 摆动序列
# https://leetcode-cn.com/problems/wiggle-subsequence/
# 思路：动态规划 & 贪心

# todo


def wiggle_max_length1(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n

    up = [1] + [0] * (n - 1)
    down = [1] + [0] * (n - 1)
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up[i] = max(up[i - 1], down[i - 1] + 1)
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            up[i] = up[i - 1]
            down[i] = max(up[i - 1] + 1, down[i - 1])
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[n - 1], down[n - 1])


def wiggle_max_length2(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n

    up = down = 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up = max(up, down + 1)
        elif nums[i] < nums[i - 1]:
            down = max(up + 1, down)

    return max(up, down)



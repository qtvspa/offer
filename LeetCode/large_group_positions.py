
# 输出字符串中较大分组的位置
# https://leetcode-cn.com/problems/positions-of-large-groups/
# 思路：一次遍历即可

from typing import List


def large_group_positions(s: str) -> List[List[int]]:

    result = []
    n, count = len(s), 1

    for i in range(n):
        if i + 1 == n or s[i] != s[i + 1]:
            if count > 2:
                result.append([i - count + 1, i])
            count = 1
        else:
            count += 1

    return result


if __name__ == '__main__':

    print(large_group_positions('abcdddeeeeaabbbcd'))

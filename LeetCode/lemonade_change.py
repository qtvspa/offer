

# 柠檬水找零
# https://leetcode-cn.com/problems/lemonade-change/
# 思路：简单逻辑题

from typing import List


def lemonade_change(bills: List[int]) -> bool:

    five_count = 0
    ten_count = 0

    for b in bills:
        if b == 5:
            five_count += 1
        elif b == 10:
            if not five_count:
                return False
            else:
                five_count -= 1
                ten_count += 1
        else:
            if ten_count >= 1 and five_count >= 1:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True

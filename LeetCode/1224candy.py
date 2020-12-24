from typing import List

# 分发糖果
# https://leetcode-cn.com/problems/candy/


# 方法一：二次遍历
def candy1(ratings: List[int]) -> int:

    # 左规则：当ratings[i - 1] < ratings[i] 时
    # i 号孩子的糖果数量将比 i - 1 号孩子的糖果数量多
    n = len(ratings)
    left = [0] * n
    for i in range(n):
        if i > 0 and ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1

    # 右规则：当ratings[i] > ratings[i + 1] 时
    # i 号孩子的糖果数量将比 i + 1 号孩子的糖果数量多
    right = ret = 0
    for i in range(n - 1, -1, -1):
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1

        # 每个孩子最终分得的糖果数量为两个数量的最大值
        ret += max(left[i], right)

    return ret


# 方法二：递增递减序列
def candy2(ratings: List[int]) -> int:

    n = len(ratings)
    ret = 1
    # 递增序列长度、递减序列长度、前一个孩子分配的糖果数量
    inc, dec, pre = 1, 0, 1

    for i in range(1, n):
        # 如果当前孩子比前一孩子分数高 视为处于递增序列 则直接将糖果数量+1 或分发与相同的糖果
        if ratings[i] >= ratings[i - 1]:
            dec = 0
            pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
            ret += pre
            inc = pre
        else:
            # 否则直接分配给当前孩子1个糖果
            pre = 1
            # 并把该孩子所在的递减序列中所有的孩子都再多分配1个糖果
            dec += 1
            # 若当前的递减序列长度和上一个递增序列等长
            # 需要把最近的递增序列的最后一个孩子也并进递减序列中
            if dec == inc:
                dec += 1
            ret += dec

    return ret


if __name__ == '__main__':
    print(candy1([1, 0, 2]))
    print(candy2([1, 0, 2]))

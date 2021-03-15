# -*- coding:utf-8 -*-

"""
矩阵中的路径
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
思路：dfs递归+回溯
"""

from typing import List


def dfs(board, i, j, word):
    # 深度优先搜索
    if not word:
        return True

    # 检查角标边界条件 以及 word首字母是否与当前元素相等
    if (i < 0 or j < 0
            or i >= len(board) or j >= len(board[0])
            or word[0] != board[i][j]):
        return False

    first_letter = board[i][j]
    # 将有效元素标记为 true
    board[i][j] = True
    # 向四个方向递归搜索
    res = (dfs(board, i + 1, j, word[1:])
           or dfs(board, i - 1, j, word[1:])
           or dfs(board, i, j + 1, word[1:])
           or dfs(board, i, j - 1, word[1:]))
    # 还原标记元素的值
    board[i][j] = first_letter
    return res


def exist(board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


def get_max_len(l: List[int]):
    all_ans = []
    start, end, dp, max_sum = 0, 0, 0, -1
    if l:
        dp = l[0]

    for i in range(1, len(l)):
        if dp > 0 and l[i] > 0:
            dp += l[i]
            end = i
        else:
            all_ans.append((start, end))
            dp = l[i]
            start = i
        if dp > max_sum:
            max_sum = dp
            all_ans.append((start, i))

    return all_ans


if __name__ == '__main__':

    print(get_max_len([1,0,1,1,0,1,1,1]))

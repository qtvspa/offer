from typing import List
import copy
# 旋转（图像）矩阵
# https://leetcode-cn.com/problems/rotate-image/
# 思路：找规律


# 方法一 使用辅助数组
def rotate(matrix: List[List[int]]) -> None:
    import copy
    n = len(matrix)
    matrix_new = copy.deepcopy(matrix)

    # 矩阵中第 i 行第 j 个元素，旋转后，它出现在倒数第 i 列的第 j 个位置
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]

    matrix[:] = matrix_new


# 方法二 原地自旋
def rotate2(matrix: List[List[int]]) -> None:

    n = len(matrix)

    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

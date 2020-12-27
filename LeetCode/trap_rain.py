from typing import List

# 接雨水
# https://leetcode-cn.com/problems/trapping-rain-water/


# 方法一：暴力法
# 计算每个下标 i 的上方分别可以接多少雨水，然后累加
# 时间复杂度O(n2) 空间复杂度O(1)
def trap(height: List[int]) -> int:

    ans = 0
    for i in range(len(height)):
        max_left, max_right = 0, 0

        # 寻找 max_left
        for j in range(0, i):
            max_left = max(max_left, height[j])

        # 寻找 max_right
        for j in range(i, len(height)):
            max_right = max(max_right, height[j])

        if min(max_left, max_right) > height[i]:
            ans += min(max_left, max_right) - height[i]

    return ans


# 方法二：动态规划
# 避免暴力法的重复计算 用两个数组来存储max_left和max_right
# 时间复杂度O(n) 空间复杂度O(n)
def trap2(height: List[int]) -> int:

    if not height:
        return 0

    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    ans = 0

    # 初始化
    max_left[0] = height[0]
    max_right[n-1] = height[n-1]
    # 设置备忘录，分别存储左边和右边最高的柱子高度
    for i in range(1, n):
        max_left[i] = max(height[i], max_left[i-1])
    for j in range(n-2, -1, -1):
        max_right[j] = max(height[j], max_right[j+1])

    # 一趟遍历，比较每个位置可以存储多少水
    for i in range(n):
        if min(max_left[i], max_right[i]) > height[i]:
            ans += min(max_left[i], max_right[i]) - height[i]

    return ans


# 方法三：双指针
# 时间复杂度O(n) 空间复杂度O(1)
def trap3(height: List[int]) -> int:

    if not height:
        return 0

    n = len(height)
    left, right = 0, n - 1  # 指针分别位于输入数组的两端
    max_left, max_right = height[0], height[n - 1]
    ans = 0

    while left <= right:
        max_left = max(height[left], max_left)
        max_right = max(height[right], max_right)

        if max_left < max_right:
            ans += max_left - height[left]
            left += 1
        else:
            ans += max_right - height[right]
            right -= 1

    return ans


# 方法四：单调栈
def trap4(height: List[int]) -> int:

    # 维护一个递减栈，栈中保存元素下标
    stack = []
    res = 0

    for i in range(len(height)):
        # 当前元素比栈顶元素大，说明栈顶元素的右边界已找到
        # 又因为维护的是一个递减栈，栈顶下面的元素高度也大于栈顶元素，即栈顶处形成凹陷，可计算面积
        while stack and height[i] > height[stack[-1]]:
            # 记录栈顶的元素并出栈，接下来我们已经得知栈顶的左右边界，可计算此元素的面积
            top = stack.pop()
            # 把栈顶弹出后栈空，即其左边没有比他大的了，无法接水
            if not stack:
                break

            # 栈顶值面积，宽: 右(即为新比较的元素) - 左(弹出后stack-1即为其左) - 1
            # 长：左右高柱中较矮的柱子 - 栈顶高度
            # 每次面积实际上仅仅是"本元素横向可接水的面积"，又因为出栈，不会重复计算， += 计算总面积
            res += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])

        # 新比较的元素比栈顶元素矮
        # 说明未找到右边界，没形成凹陷，直接将新比较的元素入该单减栈
        stack.append(i)
    return res




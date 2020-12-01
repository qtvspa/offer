from typing import List

# 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 思路：二分法（需要注意边界条件）


def search(nums: List[int], target: int) -> List[int]:

    def find_border(nums, target):
        """ 二分法找到左边界 """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] >= target:
                right = mid - 1
        return left

    i = find_border(nums, target)
    j = find_border(nums, target + 1)

    # 校验左边界是否在数组中
    if i == len(nums) or nums[i] != target:
        return [-1, -1]
    else:
        return [i, j - 1]


if __name__ == '__main__':
    result = search([1, 2, 2, 3, 4, 4, 4, 6], 4)
    print(result)

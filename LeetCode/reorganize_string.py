import collections
import heapq

# 重构字符串
# https://leetcode-cn.com/problems/reorganize-string/
# 思路：构建大顶堆 + 贪心算法


def reorganize_string(s: str) -> str:
    if len(s) < 2:
        return s

    # 提取每个字母出现的次数
    length = len(s)
    counts = collections.Counter(s)
    max_count = max(counts.items(), key=lambda x: x[1])[1]

    # 如果存在一个字母的出现次数大于 (n+1)/2，则无法重新排布字母使得相邻的字母都不相同，直接返回空字符串
    if max_count > (length + 1) // 2:
        return ""

    # 使用出现次数大于 0 的字母构建最大堆
    queue = [(-x[1], x[0]) for x in counts.items()]
    heapq.heapify(queue)
    ans = list()

    while len(queue) > 1:
        # 每次从最大堆取出两个字母，拼接到重构的字符串
        _, letter1 = heapq.heappop(queue)
        _, letter2 = heapq.heappop(queue)
        ans.extend([letter1, letter2])

        # 然后将两个字母的出现次数分别减 1
        counts[letter1] -= 1
        counts[letter2] -= 1

        # 将剩余出现次数大于 0 的字母 重新加入最大堆
        if counts[letter1] > 0:
            heapq.heappush(queue, (-counts[letter1], letter1))
        if counts[letter2] > 0:
            heapq.heappush(queue, (-counts[letter2], letter2))

        print(queue)

    # 如果最大堆变成空，则已经完成字符串的重构
    # 如果最大堆剩下 1 个元素，则取出最后一个字母，拼接到重构的字符串
    if queue:
        ans.append(queue[0][1])

    return "".join(ans)


if __name__ == '__main__':
    print(reorganize_string('aabbc'))

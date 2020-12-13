from collections import deque

# 参议院投票
# https://leetcode-cn.com/problems/dota2-senate/
# 思路：循环队列


def predict_party_victory(senate: str) -> str:
    n = len(senate)
    radiant = deque()
    dire = deque()

    # 初始化每位参议员的序号
    for i, ch in enumerate(senate):
        if ch == "R":
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        # 比较序号来决定出场顺序
        if radiant[0] < dire[0]:
            # +n 的目的是下一轮保持原有顺序
            radiant.append(radiant[0] + n)
        else:
            dire.append(dire[0] + n)
        radiant.popleft()
        dire.popleft()

    return "Radiant" if radiant else "Dire"


if __name__ == '__main__':
    print(predict_party_victory('DDRRDDRDRR'))

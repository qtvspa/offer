from collections import Counter

# 移除字符串中的重复字母
# https://leetcode-cn.com/problems/remove-duplicate-letters/
# 思路：单调栈 同时需要注意特殊情况


def remove_duplicate_letters(s: str) -> str:

    result_stack = []
    # 记录每个字母出现的次数
    s_counter = Counter(s)

    for ss in s:
        # 如果该字母已经存在于栈 则不需要入栈
        if ss in result_stack:
            s_counter[ss] -= 1
            continue
        else:
            # 这里栈为空时 直接将该字母入栈 同时将该字母的后续出现次数-1
            if not result_stack:
                s_counter[ss] -= 1
                result_stack.append(ss)
            # 栈不为空时
            else:
                # 将该字母的后续出现次数-1
                s_counter[ss] -= 1
                # 满足后续位置上还有栈顶字母且栈顶字母大于当前字母时 弹出栈顶元素
                while (result_stack
                       and ord(result_stack[-1]) > ord(ss)
                       and result_stack[-1] in s_counter
                       and s_counter[result_stack[-1]] > 0):
                    result_stack.pop()
                result_stack.append(ss)

    return ''.join(result_stack)


if __name__ == '__main__':
    print(remove_duplicate_letters("ecbacba"))

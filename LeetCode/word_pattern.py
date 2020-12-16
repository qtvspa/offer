
# https://leetcode-cn.com/problems/word-pattern/
# 思路：哈希表


def word_pattern(pattern: str, s: str) -> bool:
    pattern_list = list(pattern)
    s_list = s.split(' ')

    if not len(pattern_list) == len(s_list):
        return False

    a_dict = {}

    for i in range(len(s_list)):
        if not a_dict.get(pattern_list[i]):
            a_dict[pattern_list[i]] = s_list[i]
        else:
            if not a_dict[pattern_list[i]] == s_list[i]:
                return False

    if not len(list(set(a_dict.keys()))) == len(list(set(a_dict.values()))):
        return False

    return True


if __name__ == '__main__':
    print(word_pattern('abba', 'aa aa aa aa'))

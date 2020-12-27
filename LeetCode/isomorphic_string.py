
# 同构字符串
# https://leetcode-cn.com/problems/isomorphic-strings/
# 思路：哈希表


def is_isomorphic(s: str, t: str) -> bool:

    tmp_dict = {}
    for z in zip(s, t):
        print(z[0], z[1], tmp_dict)
        if not z[0] in tmp_dict:
            tmp_dict[z[0]] = z[1]
        else:
            if not tmp_dict[z[0]] == z[1]:
                return False

    if not len(tmp_dict) == len(list(set(t))):
        print(tmp_dict, list(set(s)))
        return False

    return True


if __name__ == '__main__':
    print(is_isomorphic('er', 'qq'))

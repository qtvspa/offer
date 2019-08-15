# -*- coding:utf-8 -*-

""" 实现⼀个函数，判断helloworld是否是给定字符串的不连续子串
    即helloworld的每个字母均在给定字符串中出现，并且需要保持先后顺序但可以允许不相邻
    如helllllllo wwwwwwworld 符合条件,
    但helolllllworld不符合条件 """


if __name__ == '__main__':
    s = 'dsasdrfsdqwwheqwcdllloasda sword'
    pattern = 'helloworld'
    if len(s) < len(pattern):
        print('false')
    the_list = []
    for i in range(len(pattern)):
        if i > 0:
            if pattern[i] in s[the_list[i-1]+1:]:
                the_list.append(the_list[i-1]+s[the_list[i-1]+1:].index(pattern[i])+1)
                if the_list[i] < the_list[i-1]:
                    print('false')
                    break
            else:
                print('false')
                break
        else:
            if pattern[i] in s:
                the_list.append(list(s).index(pattern[i]))
    if len(the_list) == len(pattern):
        print('true')

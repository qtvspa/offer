# -*- coding:utf-8 -*-

""" 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
    模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。"""


""" 思路
    当pattern为空 且s为空时应返回True
    当pattern为空 且s不为空时应返回False
    当pattern的第一位为'.' 或者 pattern的第一位与s的第一位相等时
        将s[1]与pattern[1]进行匹配
    当pattern的第二位为*时 即代表pattern的第一位字符可以出现0-N次
        此时如果s[0]与pattern[0]相等 且pattern[0]不为'.' 
            跳过pattern的前两位 将s[1:]与pattern[2:]进行匹配
        此时如果s[0]与pattern[0]相等 且pattern[0]为'.'
            当*代表0次时
                跳过pattern的前两位 将s与pattern[2:]进行匹配
            当*代表1-N次时：
                跳过pattern的前两位 将s[1:]与pattern进行匹配      
"""
import re


def match(s, pattern):
    # write code here
    if len(s) == 0 and len(pattern) == 0:
        return True
    if len(s) > 0 and len(pattern) == 0:
        return False
    if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
        return match(s[1:], pattern[1:])
    if len(pattern) > 1 and pattern[1] == '*':
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return match(s, pattern[2:]) or match(s[1:], pattern[2:]) or match(s[1:], pattern)
        else:
            return match(s, pattern[2:])

    return False



if __name__ == '__main__':

    # pattern = re.compile('^a.a$')
    inputs = 'aaa'
    # result = re.search(pattern, inputs)
    result = match('aaa', 'a.a')
    print(result)
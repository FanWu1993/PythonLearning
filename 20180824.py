# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def char2num(c):
        return DIGITS[c]
    def fn(x,y):
        return x * 10 + y
    n = s.index('.')
    s1 = reduce(fn, map(char2num, s[:n]))
    s2 = reduce(fn, map(char2num, s[n+1:]))
    n = 1
    while n<s2:
        n = n * 10
    return s1 + s2 / n
    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
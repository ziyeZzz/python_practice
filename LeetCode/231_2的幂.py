'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 2^0 = 1

示例 2:
输入: 16
输出: true
解释: 2^4 = 16

示例 3:
输入: 218
输出: false
'''
num = 218
def isPowerOfTwo(n):
    while n>1:
        if(n%2==0):
            n=n/2
        else:
            return False
    return True
print(isPowerOfTwo(num))
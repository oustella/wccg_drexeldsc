# Week-1 : https://app.codesignal.com/challenge/mXCWzh37ibxEY822h
"""
# Solution1 - did not pass time limit
def countSumOfTwoRepresentations3(n, l, r):
    numbersList = range(l,r+1)
    result = 0
    for a in numbersList:
        b = n - a
        if b in numbersList and b >= a:
            result += 1
    return result
"""
##################################
"""
Solution2 - did not pass time limit
def countSumOfTwoRepresentations3(n, l, r):
    result = 0
    for a in range(l,r+1):
        b = n - a
        if b >= l and b <= r and b >= a:
            result += 1
    return result
"""
###############################

#Solution3 - Passed the time limit

import math
def countSumOfTwoRepresentations3(n, l, r):
    x = math.ceil(n/2)
    return max(0, min(x-l , r-x) + (n+1)%2)
#For reference - https://qelifeblog.wordpress.com/2017/06/25/codefights-count-sum-of-two-representations-2/




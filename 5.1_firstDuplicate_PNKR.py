#https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q
"""
# Solution1 did not pass time limit
def firstDuplicate(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
        else:
            return i
    return -1
"""
# Solution2 executed with in time limit
def firstDuplicate(a):
    x = set()
    for i in a:
        if i in x:
            return i
        x.add(i)
    return -1



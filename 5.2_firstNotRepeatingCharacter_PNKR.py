#https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC
"""
#This solution did not pass time limit
def firstNotRepeatingCharacter(s):
    x = set()
    for i in s:
        if s.count(i) == 1:
            return i
    return '_'
"""
#passed time limit
def firstNotRepeatingCharacter(s):
    d = {i : (s.count(i), s.index(i)) for i in set(s)}
    x = sorted(d.items(), key = lambda x:x[1])
    if x[0][1][0] == 1:
        return x[0][0]
    else:
        return '_'
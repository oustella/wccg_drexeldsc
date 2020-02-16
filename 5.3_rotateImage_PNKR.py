#https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB
"""
#passed time limit
def rotateImage(a):
    R = [[] for _ in range(len(a))]
    for i in range(0,len(a)):
        for j in range(len(a)-1,-1,-1):
            R[i].append(a[j][i])
    return R
"""
#passed all tests
def rotateImage(a):
    return [[ a[j][i] for j in range(len(a)-1,-1,-1)] for i in range(0,len(a))]
#Week2 : https://app.codesignal.com/challenge/J785w3Xu4BFzqnREg

"""
#Solution1 did not pass time limit
def numbersGrouping(a):
    length = len(a)
    count = 0
    groups = []
    for item in set(a):
        i = (item-1) // 10**4 + 1
        if item <= i*10**4 and i not in groups:
            groups.append(i)
            count += 1
    return count+length
"""
############################################
"""
#Solution2 passed the time limit
def numbersGrouping(a):
    length = len(a)
    a = sorted(set(a))
    numGroup = 0
    
    while a:
        bound = (a[0]-1)//pow(10,4)+1
        #print(bound)
        numGroup += 1
        while a and a[0]<=bound*pow(10,4):
            a.pop(0)
    
    return numGroup+length
"""
################################################

#Solution3 passed the time limit
def numbersGrouping(a):
    groups = [(item-1) // 10**4 for item in set(a)]
    return len(set(groups))+len(a)



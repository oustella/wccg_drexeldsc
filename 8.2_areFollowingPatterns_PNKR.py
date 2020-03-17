#https://app.codesignal.com/interview-practice/task/3PcnSKuRkqzp8F6BN

from collections import defaultdict
def areFollowingPatterns(strings, patterns):
    if len(set(strings)) == len(set(patterns)):
        d = defaultdict(list)
        for i,v in enumerate(strings):
            if strings.count(v) > 1:
                d[v].append(patterns[i])
        for i in d:
            if len(set(d[i])) != 1:
                return False
        return True
    return False